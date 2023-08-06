import multiprocessing as mp
import subprocess
import sys
import time

import pytest

from pytorch_pfn_extras.profiler import TimeSummary, get_time_summary


def test_report():
    summary = TimeSummary()
    with summary.report("foo"):
        pass
    summary.synchronize()
    with summary.summary() as s:
        assert "foo" in s[0].compute_mean()
        assert "foo.min" in s[1]
        assert "foo.max" in s[1]
    summary.finalize()


def test_report_async():
    summary = TimeSummary()
    with summary.report("afoo") as notification:
        notification.defer()
    time.sleep(0.5)
    # Explicitly call object completion
    notification.complete()
    summary.synchronize()
    with summary.summary() as s:
        stats = s[0].compute_mean()
        assert "afoo" in stats
        assert abs(0.5 - stats["afoo"]) < 2e-2
        assert abs(0.5 - s[1]["afoo.min"]) < 2e-2
        assert abs(0.5 - s[1]["afoo.max"]) < 2e-2
    summary.finalize()


def worker(summary):
    with summary.report("foo"):
        pass


@pytest.mark.skipif(
    sys.platform == 'win32',
    reason='Multiprocessing not fully supported on Windows')
def test_report_from_other_process():
    summary = TimeSummary()
    p = mp.Process(target=worker, args=(summary,))
    p.start()
    p.join()
    summary.synchronize()
    with summary.summary() as s:
        assert "foo" in s[0].compute_mean()
        assert "foo.min" in s[1]
        assert "foo.max" in s[1]
    summary.finalize()


def worker1():
    time_summary = get_time_summary()
    with time_summary.report("foo"):
        pass


@pytest.mark.skipif(
    sys.platform == 'win32',
    reason='Multiprocessing not fully supported on Windows')
def test_global_summary():
    time_summary = get_time_summary()
    time_summary.initialize()
    p = mp.Process(target=worker1)
    p.start()
    p.join()
    time_summary.synchronize()
    with time_summary.summary() as s:
        assert "foo" in s[0].compute_mean()
        assert "foo.min" in s[1]
        assert "foo.max" in s[1]


def test_clear():
    summary = TimeSummary()
    summary.add("foo", 10)
    summary.add("foo", 5)
    summary.add("foo", 15)
    summary.synchronize()
    with summary.summary(clear=True) as s:
        assert s[0].compute_mean() == {"foo": 10}
        assert s[1] == {"foo.min": 5, "foo.max": 15}
    with summary.summary(clear=True) as s:
        assert s[0].compute_mean() == {}
        assert s[1] == {}
    summary.finalize()


def test_multiprocessing_start_method():
    # Ensure that importing PPE does not initialize multiprocessing context.
    # See #238 for the context.
    subprocess.check_call([
        sys.executable,
        '-c',
        ('import multiprocessing as mp; '
         + 'import pytorch_pfn_extras; '
         + 'mp.set_start_method("spawn"); ')
    ])
