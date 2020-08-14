from fastapi import FastAPI, HTTPException
from hangar import Repository

stockboard = FastAPI()
repo_path = '~/jjmachan/stockroom-tests/stockboard-tests'
checkout = ''


@stockboard.on_event('startup')
def startup_event():
    global checkout
    repo = Repository(repo_path)
    checkout = repo.checkout()


@stockboard.get('/')
async def home():
    return {'message': 'Welcome to Home'}


@stockboard.get('/data')
async def data_view():
    """
    return a the list of Columns we have in the current repo.
    """
    columns = checkout.columns
    return_dict = {}

    for col in columns:

        return_dict[col] = {
                'len': len(columns[col]),
                'name': col,
                'dtype': str(columns[col].dtype),
                'contains_subsamples': columns[col].contains_subsamples,
                'remote_refs': columns[col].contains_remote_references,
                'layout': columns[col].column_layout,
                'schema_type': columns[col].schema_type,
                'shape': columns[col].shape,
                'backend': columns[col].backend
                }
    return return_dict


@stockboard.get('/data/{column_name}')
async def get_column(column_name, start: int = 0, end: int = 100):
    try:
        column = checkout.columns[column_name]
    except KeyError:
        raise HTTPException(status_code=400,
                            detail=f'Column {column_name} not found')

    idxs = sorted(list(column))
    samples = []
    for idx in idxs[start:end]:
        samples.append({idx: column[idx]})

    return {'samples': [1, 2, 3]}
