import base64
from flask import redirect
import time


def redirect_link(app, action_client):
    @app.route('/external_link/<path:label>/<path:link>', methods=['GET', 'POST'])
    def redirect_to_link(label, link):
        start = time.time()
        event_start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))
        event_end_time = event_start_time
        use_time = 0
        event_detail = {
            'func_name': 'external_link.' + label,
            'func_parameters': [],
            'func_source_code': '',
            'func_module_name': 'external_link.' + label,
            'func_doc': '',
        }
        try:
            action_client.sync_post(event_detail, event_start_time, event_end_time, use_time)
        except Exception as e:
            print(f'Action logger: {e}')
        return redirect(base64.urlsafe_b64decode(link.encode()).decode())

    return app
