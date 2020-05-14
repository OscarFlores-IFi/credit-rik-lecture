from typing import Dict, List, Optional, Union

from utils import get_google_sheet_service


class GoogleSheetWrapper:

    def __init__(self, spreadsheet_id: str, sheet_name: str):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.sheet_service = get_google_sheet_service().values()

    def get_value(self, col: str, row: Union[str, int]):
        sheet_range = f"{self.sheet_name}!{col}{row}"
        target = self.sheet_service.get(spreadsheetId=self.spreadsheet_id, range=sheet_range)
        return target.execute().get('values')[0][0]

    def get_values(self, from_col: str, from_row: Union[str, int], to_col: str, to_row: Union[str, int]):
        if from_col == to_col and str(from_row) == str(to_row):
            return self.get_value(col=from_col, row=from_row)
        sheet_range = f"{self.sheet_name}!{from_col}{from_row}:{to_col}{to_row}"
        target = self.sheet_service.get(spreadsheetId=self.spreadsheet_id, range=sheet_range)
        if str(from_row) == str(to_row):
            return target.execute().get('values')[0]
        if from_col == to_col:
            return [l[0] for l in target.execute().get('values')]
        return target.execute().get('values')

    def update_values(self, values: Union[str, List], from_col: str, from_row: Union[str, int],
                      to_col: str, to_row: Union[str, int]):
        if from_col == to_col and str(from_row) == str(to_row):
            return self.update_value(value=values, col=from_col, row=from_row)
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
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = "METADATA"

    @property
    def table(self) -> dict:
        sheet_1 = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name=self.sheet_name)
        sheet_name = sheet_1.get_value(col="D", row=3)
        from_col = sheet_1.get_value(col="E", row=3)
        from_row = int(sheet_1.get_value(col="F", row=3))
        to_col = sheet_1.get_value(col="G", row=3)
        to_row = int(sheet_1.get_value(col="H", row=3))
        sheet_2 = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name=sheet_name)
        t = sheet_2.get_values(from_col, from_row, to_col, to_row)
        return {l[0]: l[1] for l in t}

    @property
    def probability_of_default(self) -> float:
        value = self.table
        values = list(value.keys())
        return float(value[values[1]])

    @property
    def loss_given_default(self) -> float:
        value = self.table
        values = list(value.keys())
        return float(value[values[2]])

    @property
    def loan_amount(self) -> float:
        value = self.table
        values = list(value.keys())
        return float(value[values[3]])

    @property
    def loan_terms(self) -> int:
        value = self.table
        values = list(value.keys())
        return int(value[values[4]])

    @property
    def loan_marr(self) -> float:
        value = self.table
        values = list(value.keys())
        return float(value[values[5]])

    @property
    def client_min_rate(self) -> float:
        value = self.table
        values = list(value.keys())
        return float(value[values[6]])

    @property
    def client_max_rate(self) -> float:
        value = self.table
        values = list(value.keys())
        return float(value[values[7]])

    @property
    def search_samples(self) -> int:
        value = self.table
        values = list(value.keys())
        return int(value[values[8]])


class RateValue:
    RESOURCE_ID = "VALUE_EXPECTED_RATE"

    def __init__(self, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = "METADATA"

    def update(self, value: str):
        sheet_1 = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name=self.sheet_name)
        sheet_name = sheet_1.get_value(col="D", row=4)
        col = sheet_1.get_value(col="E", row=4)
        row = int(sheet_1.get_value(col="F", row=4))
        sheet_2 = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name=sheet_name)
        sheet_2.update_value(value, col, row)


class RequestValue:
    RESOURCE_ID = "VALUE_REQUEST"

    def __init__(self, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = "METADATA"

    def update(self, value: str):
        sheet_1 = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name=self.sheet_name)
        sheet_name = sheet_1.get_value(col="D", row=5)
        col = sheet_1.get_value(col="E", row=5)
        row = int(sheet_1.get_value(col="F", row=5))
        sheet_2 = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name=sheet_name)
        sheet_2.update_value(value, col, row)


class ResultTable:
    RESOURCE_ID = "TABLE_RESULT"

    def __init__(self, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = "METADATA"

    def update(self, values: list):
        sheet_1 = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name=self.sheet_name)
        sheet_name = sheet_1.get_value(col="D", row=6)
        from_col = sheet_1.get_value(col="E", row=6)
        from_row = int(sheet_1.get_value(col="F", row=6))
        to_col = sheet_1.get_value(col="G", row=6)
        to_row = from_row+ConfigTable(self.spreadsheet_id).loan_terms+1
        sheet_2 = GoogleSheetWrapper(spreadsheet_id=self.spreadsheet_id, sheet_name=sheet_name)
        header = [['time', 'Balance', 'Payment', 'Interest', 'Annuity', 'IRR', 'Expected Loss', 'Prob_default']]
        header.extend(values)
        sheet_2.update_values(header, from_col, from_row, to_col, to_row)
