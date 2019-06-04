from sys import stdin
import re

res = dict()
events = {
    'Error occurred during request processing': 'req-err',
    'responseToReturn exception': 'resp-err',
    'Error occurred during response processing.':'up-resp-err',
    'Target returned unsuccessful response:':'bad-http-code',
    'Forwarding response from upstream server':'fwd-bad-code',
    'Returning response stub':'ret-stub'
}
for line in stdin:
    match = re.search(r'\[ireq_(\d+)\]', line)
    if match:
        req = match.group(1)
        timestamp = re.search(r'^([\d-]+ [\d:,]+) ', line).group(1)
        fwdMatch = re.search(r'Forwarding request to (\S+)', line)
        if fwdMatch:
            v = res.setdefault(req, list())
            v.append({'type': 'fwd',
                      'time': timestamp,
                      'dst': fwdMatch.group(1)})
        elif 'Received request' in line:
            v = res.setdefault(req, list())
            v.append({'type': 'receive',
                      'time': timestamp})
        elif 'Upstream response successfully returned code' in line:
            v = res.setdefault(req, list())
            v.append({'type': 'upstream-return',
                      'time': timestamp})
        elif 'Headers has been sent' in line:
            v = res.setdefault(req, list())
            v.append({'type': 'headers-sent',
                      'time': timestamp})
        elif 'Body has been sent' in line:
            v = res.setdefault(req, list())
            v.append({'type': 'body-sent',
                      'time': timestamp})
        elif 'Response complete' in line:
            v = res.setdefault(req, list())
            v.append({'type': 'response-complete',
                      'time': timestamp})
        else:
            found=False
            for k, v in events.items():
                if k in line:
                    v = res.setdefault(req, list())
                    v.append({'type': v,
                              'time': timestamp})
                    found = True
            if not found:
                print("No match: " + line)
                break

print(len(res))