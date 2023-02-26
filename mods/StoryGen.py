from bugsplat import BugSplat

bugsplat = BugSplat('summersphinx_duck_com', 'CodeRandom3', '0.1')

try:
    lkjlkj
except Exception as e:
    bugsplat.post(
        e,
        additional_file_paths=[],
        app_key='other key!',
        description='other description!',
        email='summersphinx@duck.com',
        user='Gavin'
    )