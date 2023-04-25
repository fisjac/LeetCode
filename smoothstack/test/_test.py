import pytest
from report_conflicts import report_conflicts

no_conflicts = ['0800,90','1000,30', '1430,60']
start_conflicts = ['0830,60','0900,30']
end_conflicts = ['0900,60','0830,45']
total_overlap = ['0745,90','0815,30']

class TestClass:

  def test_no_conflicts(self):
    answer = report_conflicts(no_conflicts)
    assert answer == 'good'

  def test_start_conflicts(self):
    answer = report_conflicts(start_conflicts)
    assert answer == 'conflict,1,30'

  def test_end_conflicts(self):
    answer = report_conflicts(end_conflicts)
    assert answer == 'conflict,1,15'

  def test_total_overlap(self):
    answer = report_conflicts(total_overlap)
    assert answer == 'conflict,1,30'
