"""Kurgusal, tek günlük CSV için eğitim amaçlı olay-zamanlı tespit.

Üretim SIEM kuralı değildir. Geç gelen kayıt, tekrar ve alarm bastırma yönetmez.
"""
import csv
import json
from datetime import datetime
from pathlib import Path


def seconds(value):
    t = datetime.strptime(value, '%H:%M:%S')
    return t.hour * 3600 + t.minute * 60 + t.second


def detect(rows, window=300, threshold=5, followup=300):
    events = sorted(rows, key=lambda r: (seconds(r['time']), r['id']))
    logins = [r for r in events if r['source'] == 'identity' and r['event'] == 'login']
    failures = [r for r in logins if r['result'] == 'failure']
    successes = [r for r in logins if r['result'] == 'success']
    candidates = []
    for end in failures:
        end_time = seconds(end['time'])
        group = [r for r in failures
                 if r['src_ip'] == end['src_ip']
                 and end_time - window < seconds(r['time']) <= end_time]
        users = sorted({r['user'] for r in group})
        if len(users) < threshold:
            continue
        matches = []
        for success in successes:
            success_time = seconds(success['time'])
            if (success['src_ip'] == end['src_ip']
                    and success['user'] in users
                    and end_time < success_time <= end_time + followup):
                matches.append({'event_id': success['id'], 'user': success['user'],
                                'time': success['time'], 'session_id': success['session_id']})
        candidates.append({'window_end': end['time'], 'src_ip': end['src_ip'],
                           'attempts': len(group), 'targeted_users': len(users),
                           'users': users, 'evidence': [r['id'] for r in group],
                           'success_matches': matches})
    return candidates


if __name__ == '__main__':
    with Path(__file__).with_name('olaylar.csv').open(newline='') as f:
        print(json.dumps(detect(list(csv.DictReader(f))), ensure_ascii=False, indent=2))
