from flask import Flask, render_template, request, Response
import subprocess
import re
from kubernetes import client, config

app = Flask(__name__)


config.load_kube_config()


@app.route('/')
def index():
    return render_template('choose_interval.html')


def update_cronjob_schedule(interval):
    with open('backup-cronjob.yaml', 'r') as file:
        cronjob_yaml = file.read()

    updated_yaml = re.sub(r'schedule: ".*"', f'schedule: "*/{interval} * * * *"', cronjob_yaml)
    
    with open('backup-cronjob-updated.yaml', 'w') as file:
        file.write(updated_yaml)


@app.route('/schedule_backup', methods=['POST'])
def schedule_backup():
    interval = request.form['interval']
    print(interval)
    update_cronjob_schedule(interval)
    subprocess.run(['kubectl', 'apply', '-f', 'backup-cronjob-updated.yaml'])
    
    return 'Backup scheduled successfully!'



@app.route('/events')
def get_events():
    v1 = client.CoreV1Api()
    event_list = v1.list_namespaced_event(namespace="default")
    # print(event_list,v1)s
    events = []
    for event in event_list.items:
        if event.message==None:
            continue
        print(event.message)
        events.append(event.message)
    return render_template('events.html', events=events)


if __name__ == '__main__':
    app.run(debug=True)
