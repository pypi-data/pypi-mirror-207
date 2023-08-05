from __future__ import annotations

__all__ = [
		'context',
		'get_contextvar',
		'run_context',
		'set_contextvar_data',
		'context_model',
		'set_modeldata',
		'update_model_context',
		'update_context',
		'get_from_context',
		'get_from_modeldata_map',
		'database_data'
]

from functools import wraps
from anyio import create_task_group
from contextvars import copy_context, ContextVar
from detabase.constants import *
from detabase.types import *
from detabase.engine import *

context = copy_context()


def key_dict_from_list(data: list[dict]) -> dict[str, dict]:
	return {item['key']: item for item in data}


async def database_data(tables: list[str]) -> dict[str, dict]:
	result = dict()
	
	async def get_data(table: str) -> None:
		result[table] = key_dict_from_list(await ModelMap[table].fetch_all())
		
	async with create_task_group() as tks:
		for item in tables:
			tks.start_soon(get_data, item)
	
	return result


def get_contextvar(table: str):
	return ContextVar(f'{table}Var', default=dict())
	
	
def set_contextvar_data(contextvar: ContextVar, data: dict[str, dict]) -> None:
	contextvar.set(data)
	
	
def run_context(table: str):
	context.run(set_contextvar_data, ContextVarMap[table], ModelDataMap[table])
	

async def set_modeldata(table: str, query: DetaQuery = None):
	ModelDataMap[table] = {item['key']: item for item in await DetaBase(table).fetch_all(query)}


async def update_model_context(table: str, query: DetaQuery = None):
	await set_modeldata(table, query)
	run_context(table)
	
	
async def update_context(tables: list[str]) -> None:
	async with create_task_group() as tks:
		for table in tables:
			tks.start_soon(update_model_context, table)
	
	
def context_model(cls):
	@wraps(cls)
	def wrapper():
		if not cls.EXIST_PARAMS:
			raise Exception(f'Cadastrar EXIST_PARAMS para a classe {cls.class_name()}.')
		name = cls.table()
		ModelMap[name] = cls
		ContextVarMap[name] = get_contextvar(name)
		ModelDataMap[name] = dict()
		return cls
	return wrapper()


def get_from_context(table: str, key: str = None) -> dict:
	if key:
		return context.get(ContextVarMap[table])[key]
	return context.get(ContextVarMap[table])


def get_from_modeldata_map(table: str, key: str = None) -> dict:
	if key:
		return ModelDataMap[table][key]
	return ModelDataMap[table]
	
	