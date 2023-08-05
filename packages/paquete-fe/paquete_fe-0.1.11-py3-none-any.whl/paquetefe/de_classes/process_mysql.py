import sys
import traceback
from datetime import datetime
from .de_classes.mysql_db_admin import Log, Proceso


def generate_process_id(session, tipo_proceso, origen, tipo_servicio='A'):
    try:
        now = datetime.now()
        v_proceso = Proceso(fecha_hora_inicio=now, 
                            estado='PROCESANDO', 
                            tipo_proceso=tipo_proceso,
                            origen=origen,
                            tipo_servicio=tipo_servicio)
        session.add(v_proceso)
        #session.flush()
        session.commit()
        return v_proceso
    except Exception:
        traceback.print_exc()
        print("Unexpected error:", sys.exc_info()[0])
        raise


def update_process_finished(session, proceso):
    try:
        mensaje = 'Concluye el proceso de generación de lote de documentos electrónicos'
        log_register(session,
                     proceso,
                     mensaje,
                     Log.INFO)

        # Un commit final por si quedo algo pendiente de commitear
        session.commit()

    except Exception:
        traceback.print_exc()
        print("Unexpected error:", sys.exc_info()[0])
        log_register(session, 
                     proceso, 
                     f'Unexpected error: {sys.exc_info()[0]}. Detalles: {traceback.print_exc()}',
                     Log.ERROR)
    #finally:
    #    session.close()
        

def log_register(session, proceso, evento, categoria):
    try:
        now = datetime.now()
        log = Log(proceso_id=proceso, 
                  eventos=evento, 
                  categoria=categoria, 
                  fecha_hora=now)
        session.add(log)
        session.commit()
        # return log
    except Exception:
        traceback.print_exc()
        print("Unexpected error:", sys.exc_info()[0])
        # raise


def update_process_state(session, proceso, estado):
    try:
        log_register(session, 
                     proceso.id, 
                     f'El proceso cambia al estado {estado}', 
                     Log.INFO)
        proceso.estado = estado
        session.commit()

    except Exception:
        traceback.print_exc()
        print("Unexpected error:", sys.exc_info()[0])
        log_register(session, 
                     proceso.id, 
                     f'Unexpected error: {sys.exc_info()[0]}. Detalles: {traceback.print_exc()}',
                     Log.ERROR)
        

