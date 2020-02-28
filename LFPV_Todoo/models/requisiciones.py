# -*- coding: utf-8 -*-
#BY: ING.LUIS FELIPE PATERNINA VITAL - TODOO SAS.

from odoo import fields,models,api



cajacom = [
    ('7000016 CAJA DE COMPENSACION FAMILIAR', '7000016 CAJA DE COMPENSACION FAMILIAR'),
    ('7000017 CAJA DE COMPENSACION FAMILIAR DEL', '7000017 CAJA DE COMPENSACION FAMILIAR DEL'),
    ('7000018 CAJA DE COMPENSACION FAMILIAR DE', '7000018 CAJA DE COMPENSACION FAMILIAR DE'),
    ('7000019 CAJA DE COMPENSACION FAMILIAR DE', '7000019 CAJA DE COMPENSACION FAMILIAR DE'),
    ('7000020 CAJA DE COMPENSACION FAMILIAR DEL', '7000020 CAJA DE COMPENSACION FAMILIAR DEL'),
    ('7000021 CAJA COMPENSACION FAMILIAR CAFAM', '7000021 CAJA COMPENSACION FAMILIAR CAFAM'),
    ('7000022 CCF CAJASAN', '7000022 CCF CAJASAN'),
    ('7000023 CCF CARTAGENA', '7000023 CCF CARTAGENA'),
    ('7000024 CCF COLSUBSIDIO', '7000024 CCF COLSUBSIDIO'),
    ('7000025 CCF COMFAMILIAR GUAJIRA', '7000025 CCF COMFAMILIAR GUAJIRA'),
    ('7000026 CCF COMFAMILIAR RISARALDA', '7000026 CCF COMFAMILIAR RISARALDA'),
    ('7000027 CCF COMFANDI', '7000027 CCF COMFANDI'),
    ('7000028 CCF COMFENALCO ANTIOQUIA', '7000028 CCF COMFENALCO ANTIOQUIA'),
    ('7000029 CCF COMFENALCO CARTAGENA', '7000029 CCF COMFENALCO CARTAGENA'),
    ('7000030 CCF COMFENALCO SANTANDER', '7000030 CCF COMFENALCO SANTANDER'),
    ('7000032 CCF CONFANORTE', '7000032 CCF CONFANORTE'),
    ('7000033 CCF CORDOBA', '7000033 CCF CORDOBA'),
    ('7000034 CCF DE ANTIOQUIA COMFAMA', '7000034 CCF DE ANTIOQUIA COMFAMA'),
    ('7000035 CCF DE BARRANCABERMEJA', '7000035 CCF DE BARRANCABERMEJA'),
    ('7000036 CCF DE BARRANQUILLA', '7000036 CCF DE BARRANQUILLA'),
    ('7000037 CCF DE BOYACA CONFABOY', '7000037 CCF DE BOYACA CONFABOY'),
    ('7000038 CAJA DE COMPENSACION FAMILIAR DE CA', '7000038 CAJA DE COMPENSACION FAMILIAR DE CA'),
    ('7000039 CCF DE CASANARE', '7000039 CCF DE CASANARE'),
    ('7000040 CCF DE HONDA', '7000040 CCF DE HONDA'),
    ('7000041 CCF DE NARIÑO', '7000041 CCF DE NARIÑO'),
    ('7000042 CCF DE SUCRE', '7000042 CCF DE SUCRE'),
    ('7000043 CCF DEL ATLANTICO', '7000043 CCF DEL ATLANTICO'),
    ('7000044 CCF DEL CAQUETA', '7000044 CCF DEL CAQUETA'),
    ('7000045 CCF DEL CAUCA', '7000045 CCF DEL CAUCA'),
    ('7000046 CCF DEL CESAR COMFACESAR', '7000046 CCF DEL CESAR COMFACESAR'),
    ('7000047 CAJA DE COMPENSACION FAMILIAR DEL', '7000047 CAJA DE COMPENSACION FAMILIAR DEL'),
    ('7000048 CCF DEL MAGDALENA', '7000048 CCF DEL MAGDALENA'),
    ('7000049 CAJA DE COMPENSACION FAMILIAR', '7000049 CAJA DE COMPENSACION FAMILIAR'),
    ('7000050 CCF FENALCO DEL TOLIMA', '7000050 CCF FENALCO DEL TOLIMA'),
    ('7000051 CCF HUILA', '7000051 CCF HUILA'),
    ('7000052 CCF REGIONAL DEL META', '7000052 CCF REGIONAL DEL META'),
    ('7000054 COMPENSAR EPS', '7000054 COMPENSAR EPS'),
    ('7000124 CAJA DE COMPENSACION FAMILIAR DE SA', '7000124 CAJA DE COMPENSACION FAMILIAR DE SA'),
    ('7000130 CAJA DE COMPENSACION FAMILIAR DEL PUTUMAYO', '7000130 CAJA DE COMPENSACION FAMILIAR DEL PUTUMAYO'),
    ('7000143 CAJA DE COMPENSACION FAMILIAR CAJACOPI ATLANTICO', '7000143 CAJA DE COMPENSACION FAMILIAR CAJACOPI ATLANTICO')
  
]



motivo_solicitud = [
    ('Renuncia Titular', 'Renuncia Titular'),
    ('Cancelación de Contrato', 'Cancelación de Contrato'),
    ('Vencimiento de Contrato', 'Vencimiento de Contrato'),
    ('Evaluación de Ascenso', 'Evaluación de Ascenso'),
    ('Ampliación de Planta', 'Ampliación de Planta'),
    ('Traslado', 'Traslado'),
    ('Sustitución Paternal', 'Sustitución Paternal'),
    ('Vacaciones', 'Vacaciones'),
    ('Funcionario Promovido', 'Funcionario Promovido'),
    ('Incapacidad / Licencia', 'Incapacidad / Licencia'),
    ('Creación de Cargo', 'Creación de Cargo'),
    ('Pensión', 'Pensión'),
    ('Otro', 'Otro')
    
  
]




class Todoo(models.Model):
    _name = 'requisiciones'
    _rec_name = 'requisiciones'
    _rec_name = 'ciudades'

    status=fields.Selection([('Borrador', 'Borrador'),('Aprobada', 'Aprobada'),('Abierta', 'Abierta'), ('Cerrada', 'Cerrada'),('Garantía','Garantía'),('Rechazada','Rechazada')], default="Borrador")

    name = fields.Char()
    solicitante=fields.Many2one('hr.employee')
    cargo_soli = fields.Char(string='Cargo del Solicitante', related='solicitante.job_id.display_name')

    emp=fields.Many2one('res.company')
    prioridad=fields.Selection([('Normal', 'Normal'),('Low', 'Low'),('High', 'High'),('Very High', 'Very High')])
    prioridad=fields.Selection([('Normal', 'Normal'),('Low', 'Low'),('High', 'High'),('Very High', 'Very High')])
    date_aper = fields.Datetime(string='Order Date', required=True, readonly=True, index=True,  copy=False, default=fields.Datetime.now, help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.")
    
    jefe_inmediato=fields.Many2one('hr.employee')
    cargo_solicitado=fields.Many2one('hr.job')
    catidad_vacantes=fields.Integer(string="Cantidad de Vacantes")
    Generos=fields.Selection([('Masculino', 'Masculino'),('Femenino', 'Femenino'),('Indefinido', 'Indefinido')])
    ciudad=fields.Char(string="Ciudad")
    ciudades=fields.Many2one('ciudades')
    sede=fields.Char(string="Sede")
    area=fields.Char(string="Área")
    unidad_organizativa=fields.Char(string="Unidad Organizativa")
    un_organizativa=fields.Many2one('unidades')
    centro_costo_facturable=fields.Selection([('Si', 'Si'),('No', 'No'),('No Aplica','No Aplica')])


    personal_a_cargo=fields.Selection([('Si', 'Si'),('No', 'No')])
    masivo=fields.Selection([('Si', 'Si'),('No', 'No')])
    requiere_entrevista=fields.Selection([('Si', 'Si'),('No', 'No')])
    requiere_prueba=fields.Selection([('Si', 'Si'),('No', 'No')])
    requiere_studio_seguridad=fields.Selection([('Si', 'Si'),('No', 'No')])


    tipo_pag=fields.Selection([('Mesual', 'Mesual'),('Quincenal', 'Quincenal')])
    turn=fields.Selection([('Fijo', 'Fijo'),('Rotativo', 'Rotativo')])
    horari=fields.Many2one('resource.calendar')
    nivel_riesgo=fields.Selection([('1-0.522%', '1-0.522%'),('2-1.044%', '2-1.044%'),('3-2.436%', '3-2.436%'),('4-4.350%', '4-4.350%')])
    arl_1=fields.Selection([('7000000 ARL SURA', '7000000 ARL SURA'),('7000073 LIBERTY SEGUROS DE VIDA S.A.', '7000073 LIBERTY SEGUROS DE VIDA S.A.'),('7000171 COMPAÑIA DE SEGUROS DE VIDA COLMENA', '7000171 COMPAÑIA DE SEGUROS DE VIDA COLMENA')])
    nivel_riesgo_arl=fields.Selection([('1', '1'),('2', '2'),('3','3'),('4','4'),('5','5')])
    caja_compensac=fields.Selection(cajacom)
    manejo_vacaciones=fields.Selection([('L-V', 'L-V'),('L-S', 'L-S')])
    manejo_incapacidades=fields.Selection([('PAGAR AL 66.66%', 'PAGAR AL 66.66%'),('PAGAR AL 100%', 'PAGAR AL 100%')])

    tipo_contrato=fields.Selection([('Fijo', 'Fijo'),('Servicios', 'Servicios'),('Indefinido', 'Indefinido'),('Obra Labor', 'Obra Labor'),('Aprendizaje', 'Aprendizaje')])
    Tiempo_de_Contrato_Inicial=fields.Integer()    
    cliente1=fields.Char(string="Cliente")
    No_Contrato_Comercial=fields.Char(string="No. Contrato Comercial")
    tiempo_contrato=fields.Integer(string="Tiempo Real del Contrato")
    rango=fields.Selection([('Días', 'Días'),('Meses', 'Meses'),('Años', 'Años')])   



    mo_solicitud=fields.Selection(motivo_solicitud)
    persona_quien_reemplaza=fields.Char(string="Person a Quien Reemplaza")
    per_quien_reemplaza=fields.Many2one('hr.employee')
    cargo_pre=fields.Selection([('Si', 'Si'),('No', 'No')])

    tipo_de_salario=fields.Selection([('Suedo Básico', 'Sueldo Básico'),('Salario Integral', 'Salario Integral'),('Apoyo Sostenimiento', 'Apoyo Sostenimiento')])
    pacto_con=fields.Selection([('Pacto Colectivo', 'Pacto Colectivo'),('Convención Colectiva de Trabajo', 'Convención Colectiva de Trabajo')])
    refer=fields.Selection([('Si', 'Si'),('No', 'No')])
    docuemnto_ref=fields.Binary(string="Documento Referido")


    aux_alimentacion=fields.Selection([('Si', 'Si'),('No', 'No')])
    Valor_Auxilio_d_Alimentación=fields.Float(string="Valor Auxilio de Alimentación")
    Auxilio_de_Alimentación_a_partir_de=fields.Selection([('FECHA DE INGRESO', 'FECHA DE INGRESO'),('1 MES', '1 MES'),('2 MESES','2 MESES'),('3 MESES','3 MESES'),('4 MESES','4 MESES')])    
    aux_rodamiento=fields.Selection([('Si', 'Si'),('No', 'No')])
    Valor_Auxili_de_Rodamiento=fields.Float(string="Valor Auxilio de Rodamiento")
    Auxilio_de_Rodamiento_a_partir_de=fields.Selection([('FECHA DE INGRESO', 'FECHA DE INGRESO'),('1 MES', '1 MES'),('2 MESES','2 MESES'),('3 MESES','3 MESES'),('4 MESES','4 MESES')]) 
    aux_celular=fields.Selection([('Si', 'Si'),('No', 'No')])
    Valor_Auxilio_de_Celular=fields.Float(string="Valor Auxilio de Celular")
    Auxilio_de_Celular_a_partir_de=fields.Selection([('FECHA DE INGRESO', 'FECHA DE INGRESO'),('1 MES', '1 MES'),('2 MESES','2 MESES'),('3 MESES','3 MESES'),('4 MESES','4 MESES')]) 
   


    medicina_prepagada=fields.Selection([('Si', 'Si'),('No', 'No')])
    Valor_Medicina_Prepagada=fields.Float(string="Valor Medicina Prepagada")
    Medicina_Prepagada_a_partir_de=fields.Selection([('FECHA DE INGRESO', 'FECHA DE INGRESO'),('1 MES', '1 MES'),('2 MESES','2 MESES'),('3 MESES','3 MESES'),('4 MESES','4 MESES')]) 
    bonos=fields.Selection([('Si', 'Si'),('No', 'No')])
    Valor_Bonos=fields.Float(string="Valor Bonos")
    Bonos_a_partir_de=fields.Selection([('FECHA DE INGRESO', 'FECHA DE INGRESO'),('1 MES', '1 MES'),('2 MESES','2 MESES'),('3 MESES','3 MESES'),('4 MESES','4 MESES')]) 
    comisiones=fields.Selection([('Si', 'Si'),('No', 'No')])
    Valor_Comisiones=fields.Float(string="Valor Comisiones")
    Comisiones_a_partir_de=fields.Selection([('FECHA DE INGRESO', 'FECHA DE INGRESO'),('1 MES', '1 MES'),('2 MESES','2 MESES'),('3 MESES','3 MESES'),('4 MESES','4 MESES')]) 
    otro=fields.Selection([('Si', 'Si'),('No', 'No')])
    cual_Otro_Beneficio=fields.Char()
    Valor_Otro_Beneficio=fields.Float()
    Otro_Beneficio_a_partir_de=fields.Selection([('FECHA DE INGRESO', 'FECHA DE INGRESO'),('1 MES', '1 MES'),('2 MESES','2 MESES'),('3 MESES','3 MESES'),('4 MESES','4 MESES')])    


    tipo_cargo=fields.Selection([('Nivel Operativo', 'Nivel Operativo'),('Mandos Medios y Nivel Admon', 'Mandos Medios y Nivel Admon'),('Alta Gerencia y Mandos ESP', 'Alta Gerencia y Mandos ESP')])
    psicologo=fields.Many2one('hr.employee')
    reclutador=fields.Many2one('hr.employee')
  

    
    observaciones=fields.Char(string="Observaciones")

 