from __future__ import annotations

import pytest
from pydantic import ValidationError

from exact_online_sdk.models.absence_registration import AbsenceRegistration
from exact_online_sdk.models.absence_registration_transaction import (
    AbsenceRegistrationTransaction,
)
from exact_online_sdk.models.costcenter import Costcenter
from exact_online_sdk.models.costunit import Costunit
from exact_online_sdk.models.department import Department
from exact_online_sdk.models.division import Division
from exact_online_sdk.models.division_class import DivisionClass
from exact_online_sdk.models.division_class_name import DivisionClassName
from exact_online_sdk.models.division_class_value import DivisionClassValue
from exact_online_sdk.models.job_group import JobGroup
from exact_online_sdk.models.job_title import JobTitle
from exact_online_sdk.models.leave_absence_hours_by_day import LeaveAbsenceHoursByDay
from exact_online_sdk.models.leave_build_up_registration import (
    LeaveBuildUpRegistration,
)
from exact_online_sdk.models.leave_registration import LeaveRegistration
from exact_online_sdk.models.schedule import Schedule


class TestAbsenceRegistration:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Employee": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "EmployeeFullName": "John Doe",
            "Division": 100,
            "Cause": 1,
            "CauseCode": "ZK",
            "Notes": "Sick leave",
        }
        obj = AbsenceRegistration.model_validate(data)
        assert str(obj.id) == "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        assert obj.employee_full_name == "John Doe"
        assert obj.cause == 1
        assert obj.notes == "Sick leave"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            AbsenceRegistration.model_validate({"UnknownField": "x"})


class TestAbsenceRegistrationTransaction:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "AbsenceRegistration": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Division": 100,
            "Hours": 8.0,
            "HoursFirstDay": 4.0,
            "HoursLastDay": 4.0,
            "Status": 0,
            "PercentageDisablement": 50.0,
        }
        obj = AbsenceRegistrationTransaction.model_validate(data)
        assert obj.hours == 8.0
        assert obj.hours_first_day == 4.0
        assert obj.status == 0
        assert obj.percentage_disablement == 50.0

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            AbsenceRegistrationTransaction.model_validate({"UnknownField": "x"})


class TestCostcenter:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Active": True,
            "Code": "CC001",
            "Description": "Main cost center",
            "Division": 100,
        }
        obj = Costcenter.model_validate(data)
        assert obj.code == "CC001"
        assert obj.active is True
        assert obj.description == "Main cost center"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            Costcenter.model_validate({"UnknownField": "x"})


class TestCostunit:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Code": "CU001",
            "Description": "Project A",
            "Division": 100,
        }
        obj = Costunit.model_validate(data)
        assert obj.code == "CU001"
        assert obj.description == "Project A"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            Costunit.model_validate({"UnknownField": "x"})


class TestDepartment:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Code": "DEP001",
            "Description": "Engineering",
            "Division": 100,
            "Costcenter": "CC001",
            "CostcenterDescription": "Main",
            "Notes": "Main department",
        }
        obj = Department.model_validate(data)
        assert obj.code == "DEP001"
        assert obj.description == "Engineering"
        assert obj.costcenter == "CC001"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            Department.model_validate({"UnknownField": "x"})


class TestDivisionClass:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "ClassNameID": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Code": "DC001",
            "Description": "Division class",
            "SequenceNr": 1,
        }
        obj = DivisionClass.model_validate(data)
        assert obj.code == "DC001"
        assert obj.sequence_nr == 1

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            DivisionClass.model_validate({"UnknownField": "x"})


class TestDivisionClassName:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Description": "Classification name",
            "DescriptionTermID": 42,
            "SequenceNr": 1,
        }
        obj = DivisionClassName.model_validate(data)
        assert obj.description == "Classification name"
        assert obj.description_term_id == 42

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            DivisionClassName.model_validate({"UnknownField": "x"})


class TestDivisionClassValue:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Class_01_ID": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Class_02_ID": "c1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Division": 100,
        }
        obj = DivisionClassValue.model_validate(data)
        assert str(obj.class_01_id) == "b1b2c3d4-e5f6-7890-abcd-ef1234567890"
        assert str(obj.class_02_id) == "c1b2c3d4-e5f6-7890-abcd-ef1234567890"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            DivisionClassValue.model_validate({"UnknownField": "x"})


class TestDivision:
    def test_parses_aliases(self) -> None:
        data = {
            "Code": 123,
            "Description": "My company",
            "Country": "NL",
            "Currency": "EUR",
            "Main": True,
            "Status": 0,
            "VATNumber": "NL123456789B01",
        }
        obj = Division.model_validate(data)
        assert obj.code == 123
        assert obj.description == "My company"
        assert obj.main is True
        assert obj.vat_number == "NL123456789B01"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            Division.model_validate({"UnknownField": "x"})


class TestJobGroup:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Code": "JG001",
            "Description": "Management",
            "Division": 100,
            "Notes": "Top level",
        }
        obj = JobGroup.model_validate(data)
        assert obj.code == "JG001"
        assert obj.description == "Management"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            JobGroup.model_validate({"UnknownField": "x"})


class TestJobTitle:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Code": "JT001",
            "Description": "Software Engineer",
            "Division": 100,
            "JobCode": "SE",
            "JobGroup": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "JobLevelFrom": 5,
            "JobLevelTo": 8,
        }
        obj = JobTitle.model_validate(data)
        assert obj.code == "JT001"
        assert obj.description == "Software Engineer"
        assert obj.job_level_from == 5
        assert obj.job_level_to == 8

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            JobTitle.model_validate({"UnknownField": "x"})


class TestLeaveAbsenceHoursByDay:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Employee": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Division": 100,
            "Hours": 8.0,
            "Status": 2,
            "Type": 0,
            "ExternalIDInt": 12345,
        }
        obj = LeaveAbsenceHoursByDay.model_validate(data)
        assert obj.hours == 8.0
        assert obj.status == 2
        assert obj.type == 0
        assert obj.external_id_int == 12345

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            LeaveAbsenceHoursByDay.model_validate({"UnknownField": "x"})


class TestLeaveBuildUpRegistration:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Employee": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Division": 100,
            "Hours": 4.0,
            "LeaveType": "c1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "LeaveTypeCode": "VAC",
            "Status": 2,
            "Notes": "Holiday buildup",
        }
        obj = LeaveBuildUpRegistration.model_validate(data)
        assert obj.hours == 4.0
        assert obj.leave_type_code == "VAC"
        assert obj.status == 2

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            LeaveBuildUpRegistration.model_validate({"UnknownField": "x"})


class TestLeaveRegistration:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Employee": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Division": 100,
            "Hours": 16.0,
            "HoursFirstDay": 8.0,
            "HoursLastDay": 8.0,
            "LeaveType": "c1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "LeaveTypeCode": "VAC",
            "Status": 2,
        }
        obj = LeaveRegistration.model_validate(data)
        assert obj.hours == 16.0
        assert obj.hours_first_day == 8.0
        assert obj.leave_type_code == "VAC"
        assert obj.status == 2

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            LeaveRegistration.model_validate({"UnknownField": "x"})


class TestSchedule:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "AverageHours": 40.0,
            "Code": "FT",
            "Description": "Full time",
            "Division": 100,
            "Employment": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "ScheduleType": 1,
            "Days": 5.0,
            "Main": 1,
            "PaymentParttimeFactor": 1.0,
        }
        obj = Schedule.model_validate(data)
        assert obj.average_hours == 40.0
        assert obj.code == "FT"
        assert obj.schedule_type == 1
        assert obj.days == 5.0
        assert obj.main == 1

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            Schedule.model_validate({"UnknownField": "x"})
