# import os
# import sys

# # get the absolute path of the directory containing this script
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # get the absolute path of the parent directory of the "money_mastery" package
# package_parent_dir = os.path.abspath(os.path.join(script_dir, ".."))

# # add the parent directory to the Python path
# sys.path.append(package_parent_dir)


# # from money_mastery.core.database import database
# from money_mastery.models.conta_model import Conta
# # from money_mastery.repository.generic_crud_databases import GenericCRUDDB
# from money_mastery.repository.generic_crud_session import GenericCRUD
# from money_mastery.core.deps import get_session, database as db
# from fastapi import Depends

# # contaRepo = GenericCRUDDB(database, Conta)
# contaRepoAlchemy = GenericCRUD(db_session=db.session(), model=Conta) # type: ignore

# # async def obter_contas():
# #     return await contaRepo.get_multi()

# # print(obter_contas.items())

# async def obter_contas():
#     teste = await contaRepoAlchemy.get_multi()
#     print(teste)

# obter_contas()

# # print(obter_contas())
