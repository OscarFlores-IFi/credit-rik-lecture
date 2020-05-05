from typing import Dict, List, Optional, Union

from utils import get_google_sheet_service


class GoogleSheetWrapper:

    def __init__(self, spreadsheet_id: str, sheet_name: str):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.sheet_service = get_google_sheet_service().values()

    def update_values(self, values: Union[str, List], from_col: str, from_row: Union[str, int],
                      to_col: str, to_row: Union[str, int]):
        if from_col == to_col and str(from_row) == str(to_row):
            return self.update_value(value=values, col=from_col, row=from_col)
        sheet_range = f"{self.sheet_name}!{from_col}{from_row}:{to_col}{to_row}"
        body = {
            "values": values
        }
        target = self.sheet_service.update(spreadsheetId=self.spreadsheet_id, range=sheet_range,
                                           valueInputOption="RAW", body=body)
        return target.execute()

    def update_value(self, value: str, col: str, row: Union[str, int]):
        sheet_range = f"{self.sheet_name}!{col}{row}"
        body = {
            "values": [[value]]
        }
        target = self.sheet_service.update(spreadsheetId=self.spreadsheet_id, range=sheet_range,
                                           valueInputOption="RAW", body=body)
        return target.execute()


class ConfigTable:
    RESOURCE_ID = "TABLE_CONFIG"

    def __init__(self, spreadsheet_id: str):
        pass

    @property
    def probability_of_default(self) -> float:
        raise NotImplementedError()

    @property
    def loss_given_default(self) -> float:
        raise NotImplementedError()

    @property
    def loan_amount(self) -> float:
        raise NotImplementedError()

    @property
    def loan_terms(self) -> int:
        raise NotImplementedError()

    @property
    def loan_marr(self) -> float:
        raise NotImplementedError()

    @property
    def client_min_rate(self) -> float:
        raise NotImplementedError()

    @property
    def client_max_rate(self) -> float:
        raise NotImplementedError()

    @property
    def search_samples(self) -> int:
        raise NotImplementedError()


class RateValue:
    RESOURCE_ID = "VALUE_EXPECTED_RATE"

    def __init__(self, spreadsheet_id: str):
        pass

    def update(self, value: str):
        pass


class RequestValue:
    RESOURCE_ID = "VALUE_REQUEST"

    def __init__(self, spreadsheet_id: str):
        pass

    def update(self, value: str):
        pass


class ResultTable:
    RESOURCE_ID = "TABLE_RESULT"

    def __init__(self, spreadsheet_id: str):
        pass

    def update(self, values: List):
        pass
