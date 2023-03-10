from fastapi import APIRouter

from .conta import router as router_conta
from .user import router as router_login

router = APIRouter(prefix='/v1')

router.include_router(router=router_login)
router.include_router(router=router_conta)
