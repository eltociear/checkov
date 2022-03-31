import unittest
from pathlib import Path

from checkov.runner_filter import RunnerFilter
from checkov.terraform.checks.resource.aws.KinesisFirehoseDeliveryStreamUsesCMK import check
from checkov.terraform.runner import Runner


class TestKinesisFirehoseDeliveryStreamUsesCMK(unittest.TestCase):
    def test(self):
        # given
        test_files_dir = Path(__file__).parent / "example_KinesisFirehoseDeliveryStreamUsesCMK"

        # when
        report = Runner().run(root_folder=str(test_files_dir), runner_filter=RunnerFilter(checks=[check.id]))

        # then
        summary = report.get_summary()

        passing_resources = {
            "aws_kinesis_firehose_delivery_stream.pass",
        }

        failing_resources = {
            "aws_kinesis_firehose_delivery_stream.fail",
            "aws_kinesis_firehose_delivery_stream.fail2",
            "aws_kinesis_firehose_delivery_stream.fail3",
            "aws_kinesis_firehose_delivery_stream.fail4",
            "aws_kinesis_firehose_delivery_stream.fail5",
            "aws_kinesis_firehose_delivery_stream.fail6",
        }

        passed_check_resources = {c.resource for c in report.passed_checks}
        failed_check_resources = {c.resource for c in report.failed_checks}

        self.assertEqual(summary["passed"], 1)
        self.assertEqual(summary["failed"], 6)
        self.assertEqual(summary["skipped"], 0)
        self.assertEqual(summary["parsing_errors"], 0)

        self.assertEqual(passing_resources, passed_check_resources)
        self.assertEqual(failing_resources, failed_check_resources)


if __name__ == "__main__":
    unittest.main()
