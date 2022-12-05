import os

from flask import Blueprint, render_template, request
from scipy.io import wavfile
from werkzeug.utils import secure_filename

from main import app
from tasks.tasks import load

from flask import send_file


bp = Blueprint('point', __name__)


@bp.route('/sound', methods=['GET', 'POST'])
def index():
    result = None
    result_file = None
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        result = load(
            sound=os.path.join(app.config['UPLOAD_FOLDER'], filename),
            sample_start=int(request.form['lower']),
            sample_end=int(request.form['upper']),
            fading_start=request.form.get('fading_start'),
            fading_end=request.form.get('fading_end'),
        )

        sample_data = result['sample_data']
        sample_rate = result['sr']
        result_file = wavfile.write(
                os.path.join(app.config['UPLOAD_FOLDER'], 'cropped.wav'),
                rate=sample_rate,
                data=sample_data,
            )

    return render_template('index.html', result=result, file=result_file)


@bp.route('/download', methods=['GET'])
def download():
    path = os.path.join(app.config['UPLOAD_FOLDER'], 'cropped.wav')
    return send_file(path, as_attachment=True)
