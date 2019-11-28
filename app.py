from flask import Flask, request, render_template, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from modelos.usuario import Usuario
from modelos.profesor import Profesor
from modelos.aula import Aula
from modelos.etapa import Etapa
from modelos.seccion import Seccion
from modelos.nivel import Nivel
from modelos.grado import Grado
from modelos.curso import Curso
from modelos.profesor_curso import ProfesorCurso
from modelos.alumno import Alumno


app = Flask(__name__)
app.config['SECRET_KEY'] = '1314/*++345347854623422342/´erewdghj´'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return Usuario.cargar_usuario(user_id)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = load_user(request.form['user-box'])
        if usuario == None:
            return render_template('login.html')
        else:
            if usuario.check_password(request.form['password-box']):
                login_user(usuario)
                return redirect(url_for('index'))
            else:
                return render_template('login.html', mensaje='Usuario y/o contraseña incorrectos')
    else:
        return render_template('login.html')


@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/asistencia', methods=['GET','POST'])
def asistencia():
    grados=Grado.cargar_grados()
    if request.method=='POST':
        if request.form['action']=='Filtrar':
            print(request.form['grado-box'], '**********************************************')
            alumnos=Alumno.filtrar_alumnos(request.form['grado-box'])
            return render_template('asistencia.html', grados=grados, alumnos=alumnos)
    else:
        return render_template('asistencia.html', grados=grados)


@app.route('/calificaciones')
def calificaciones():
    return render_template('calificaciones.html')



@app.route('/aindex')
def aindex():
    return render_template('aindex.html')


@app.route('/salir')
def salir():
    logout_user()
    return redirect('/')


@app.route('/profesores', methods=['POST', 'GET'])
def profesores():
    if request.method == 'POST':
        Profesor.registrar_profesor(request.form['dni-box'], request.form['nombres-box'], request.form['paterno-box'],request.form['materno-box'], request.form['celular-box'], request.form['correo-box'], request.form['rol-box'])
        return render_template('iprofesores.html', profesores=Profesor.cargar_profesores())
    else:
        return render_template('profesores.html')


@app.route('/aulas')
def aulas():
    aulas=Aula.cargar_aulas()
    if aulas==None:
        return render_template('aulas.html')
    else:
        return render_template('aulas.html', aulas=aulas)

@app.route('/raulas', methods=['POST', 'GET'])
def raulas():
    if request.method == 'POST':
        Aula.registrar_aula(request.form['codigo-box'],request.form['capacidad-box'], request.form['piso-box'])
        return redirect(url_for('aulas'))
    else:
        return render_template('raulas.html')


@app.route('/iprofesores')
def iprofesores():
    return render_template('iprofesores.html', profesores=Profesor.cargar_profesores())


@app.route('/eliminarAula/<codigo>')
def eliminar_aula(codigo):
    Aula.eliminar_aula(codigo)
    return redirect('/aulas')


@app.route('/eliminarProfesor/<dni>')
def eliminar_profesor(dni):
    Profesor.eliminar_profesor(dni)
    return redirect('/iprofesores')



@app.route('/etapas', methods=['POST', 'GET'])
def etapas():
    if request.method=='POST':
        Etapa.registrar_etapa(request.form['nombre-box'])
    etapas=Etapa.cargar_etapas()
    if etapas!=None:
        return render_template('etapas.html', etapas=etapas)
    else:
        return render_template('etapas.html')


@app.route('/eliminarEtapa/<nombre>')
def eliminar_etapa(nombre=''):
    Etapa.eliminar_etapa(nombre)
    return redirect('/etapas')

@app.route('/secciones', methods=['POST', 'GET'])
def secciones():
    if request.method=='POST':
        Seccion.registrar_seccion(request.form['nombre-box'])
    secciones=Seccion.cargar_secciones()
    if secciones!=None:
        return render_template('secciones.html', secciones=secciones)
    else:
        return render_template('secciones.html')

@app.route('/eliminarSeccion/<nombre>')
def eliminar_seccion(nombre=''):
    Seccion.eliminar_seccion(nombre)
    return redirect('/secciones')



@app.route('/niveles', methods=['POST', 'GET'])
def niveles():
    if request.method=='POST':
        Nivel.registrar_nivel(request.form['nombre-box'])
    niveles=Nivel.cargar_niveles()
    if niveles!=None:
        return render_template('niveles.html', niveles=niveles)
    else:
        return render_template('niveles.html')

@app.route('/eliminarNivel/<nombre>')
def eliminar_nivel(nombre=''):
    Nivel.eliminar_nivel(nombre)
    return redirect('/niveles')


@app.route('/grados', methods=['GET', 'POST'])
def grados():
    if request.method=='POST':
        Grado.registrar_grado(request.form['etapa-box'], request.form['seccion-box'], request.form['nivel-box'], request.form['aula-box'])
    etapas=Etapa.cargar_etapas()
    secciones=Seccion.cargar_secciones()
    niveles=Nivel.cargar_niveles()
    aulas=Aula.cargar_aulas()
    grados=Grado.cargar_grados()
    if grados==None:
        return render_template('grados.html', etapas=etapas, secciones=secciones, niveles=niveles, aulas=aulas)
    else:
        return render_template('grados.html', etapas=etapas, secciones=secciones, niveles=niveles, aulas=aulas, grados=grados)

@app.route('/eliminarGrado/<codigo>')
def eliminar_grado(codigo):
    Grado.eliminar_grado(codigo)
    return redirect('/grados')





@app.route('/profesoresCursos', methods=['POST', 'GET'])
def profesores_cursos():
    if request.method=='POST':
        ProfesorCurso.registrar_profesores_cursos(request.form['profesor-box'], request.form['curso-box'])
    profesores=Profesor.cargar_profesores()
    cursos=Curso.cargar_cursos()
    profesores_cursos=ProfesorCurso.mostrar_profesores_cursos()
    if profesores_cursos==None:
        return render_template('profesores_cursos.html', profesores=profesores, cursos=cursos)
    else:
        return render_template('profesores_cursos.html', profesores=profesores, cursos=cursos, profesores_cursos=profesores_cursos)







@app.route('/cursos', methods=['POST', 'GET'])
def cursos():
    if request.method=='POST':
        Curso.registrar_curso(request.form['curso-box'])
    cursos=Curso.cargar_cursos()
    if cursos==None:
        return render_template('cursos.html')
    else:
        return render_template('cursos.html', cursos=cursos)

@app.route('/eliminarCurso/<codigo>')
def eliminar_curso(codigo):
    Curso.eliminar_curso(codigo)
    return redirect('/cursos')

@app.route('/eliminarProfesorCurso/<profesor>/<curso>')
def eliminar_profesor_curso(profesor, curso):
    ProfesorCurso.eliminar_profesores_cursos(profesor, curso)
    return redirect('/profesoresCursos')



@app.route('/alumnos', methods=['POST','GET'])
def alumnos():
    if request.method=='POST':
        Alumno.registrar_alumnos(request.form['dni-box'], request.form['nombres-box'], request.form['paterno-box'], request.form['materno-box'], request.form['grado-box'], request.form['edad-box'], request.form['sexo-box'], request.form['apoderado-box'])
    grados=Grado.cargar_grados()
    alumnos=Alumno.cargar_alumnos()
    if alumnos==None:
        return render_template('alumnos.html', grados=grados)
    else:
        return render_template('alumnos.html', grados=grados, alumnos=alumnos)


@app.route('/eliminarAlumno/<dni>', methods=['POST','GET'])
def eliminar_alumno(dni):
    Alumno.eliminar_alumno(dni)
    return redirect('/alumnos')


@app.route('/horarios')
def horarios():
    profesoresCursos=ProfesorCurso.mostrar_profesores_cursos()
    return render_template('horarios.html', profesores_cursos=profesoresCursos)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8050, debug=True)
