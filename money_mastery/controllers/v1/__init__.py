from fastapi import APIRouter

from .conta import router as router_conta
from .user import router as router_login
from .entrada import router as router_entrada
from .saida import router as router_saida

router = APIRouter(prefix='/v1')

router.include_router(router=router_login)
router.include_router(router=router_conta)
router.include_router(router=router_entrada)
router.include_router(router=router_saida)
