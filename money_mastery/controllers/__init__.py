from fastapi import APIRouter

from .v1 import router as router_v1

router = APIRouter(prefix='/api')

router.include_router(router=router_v1)
