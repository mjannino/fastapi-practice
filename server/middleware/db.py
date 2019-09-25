from starlette.requests import Request
from starlette.concurrency import run_in_threadpool
from sqlalchemy.orm import sessionmaker
from ..main import app, Session


def finish_session(session):
    session.commit()
    session.close()


@app.middleware('http')
async def create_session(request: Request, call_next):
    request.state.db = session = Session()
    response = await call_next(request)
    await run_in_threadpool(finish_session, session)
    return response