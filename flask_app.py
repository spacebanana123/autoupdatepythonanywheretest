from flask import Flask, request
import git
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Test change 6'

@app.route('/update_server', methods=['POST'])
def update_server_from_git():
    if request.method != 'POST':
        return 'OK'
    else: 
        event = request.headers.get('X-GitHub-Event')
        if event == "ping":
            return json.dumps({'msg': 'Hi!'})

        if event != "push":
            return json.dumps({'msg': "Wrong event type"})


        repo = git.Repo('/home/autodeploymenttesting/mysite/')


        origin = repo.remotes.origin

        pull_info = origin.pull()

        commit_hash = pull_info[0].commit.hexsha



        build_commit = f'build_commit = "{commit_hash}"'




        print(f'{build_commit}')
        return 'Updated PythonAnywhere server to commit {commit}'.format(commit=commit_hash)








