from starlette.requests import Request
from starlette.concurrency import run_in_threadpool
from ..database import session, SessionLocal
from ..main import app


def finish_session(session):
    session.commit()
    session.close()


@app.middleware('http')
async def create_session(request: Request, call_next):
    request.state.db = session = SessionLocal()
    response = await call_next(request)
    await run_in_threadpool(finish_session, session)
    return response