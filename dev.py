#!/usr/bin/env python2

from qgic13 import app
try:
    from scss import Scss as S
    import os, glob
    def compile_scss():
        scss_shlex = os.path.join(app.name, 'static', 'scss', '*.scss')
        scss_files = glob.glob(scss_shlex)
        scss = (S().compile(open(f).read()) for f in scss_files)
        [open(f.replace('scss', 'css'), 'w').write(S().compile(open(f).read())) for f in scss_files]
        return 'compiled some scss: {}'.format(', '.join(scss_files))

except ImportError:
    compile_scss = lambda: 'pyscss not found. not compiling css.'


app.debug = True


if __name__ == '__main__':
    print(compile_scss())
    app.run()
