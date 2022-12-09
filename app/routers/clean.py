from distutils.command.clean import clean
from fastapi import APIRouter, Depends, HTTPException

from app.functions.clean.dataclean import DataClean

from .users import oauth2_scheme
from ..functions.clean import dataclean

router = APIRouter(
    prefix="/clean",
    tags=["clean"],
    dependencies=[Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)

fake_rules = {"rule_1": {"name": "Rule 1"}, "rule_2": {"name": "Rule 2"}}

@router.get("/rules")
async def get_rules():
    return DataClean.get_rules()

@router.get("/rules/{rule_id}")
async def get_rule(rule_id: str):
    if rule_id not in fake_rules:
        raise HTTPException(status_code=404, detail="Rule not found")
    return {"name": fake_rules[rule_id]["name"], "rule_id": rule_id}

@router.post("/{string_to_clean}")
async def get_clean_item(string_to_clean: str):
    rules = DataClean.get_rules()
    dump = DataClean.clean_functional_role(rules, string_to_clean)
    print(type(dump))
    return dump
