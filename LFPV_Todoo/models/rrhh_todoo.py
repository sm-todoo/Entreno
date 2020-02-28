# -*- coding: utf-8 -*-
#BY: LUIS FELIPE PATERNINA VITAL - TODOO SAS.

from odoo import fields,models,api
import re
from odoo.exceptions import ValidationError
from datetime import datetime,date,timedelta



alphabet = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
    ('G', 'G'),
    ('H', 'H'),
    ('I', 'I'),
    ('J', 'J'),
    ('K', 'K'),
    ('L', 'L'),
    ('M', 'M'),
    ('N', 'N'),
    ('Ñ', 'Ñ'),
    ('O', 'O'),
    ('P', 'P'),
    ('Q', 'Q'),
    ('R', 'R'),
    ('S', 'S'),
    ('T', 'T'),
    ('U', 'U'),
    ('V', 'V'),
    ('W', 'W'),
    ('X', 'X'),
    ('Y', 'Y'),
    ('Z', 'Z')
]


av = [
    ('AV', 'AV'),
    ('CL', 'CL'),
    ('CR', 'CR'),
    ('TRANS', 'TRANS'),
    ('DIAG', 'DIAG')
    
]


dire = [
    ('BIS', 'BIS'),
    ('BISSUR', 'BISSUR'),
    ('BISNORTE', 'BISNORTE'),
    ('BISOESTE', 'BISOESTE'),
    ('SUR', 'SUR'),
    ('NORTE', 'NORTE')   
]



tallazapatos = [
    ('30', '30'),
    ('31', '31'),
    ('32', '32'),
    ('33', '33'),
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44')
  
]


grupo_san = [
    ('AB-', 'AB-'),
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-')   
]



tipo_vivienda = [
    ('Casa', 'Casa'),
    ('Apartamento', 'Apartamento'),
    ('Cuarto(s) en inquilinato', 'Cuarto(s) en inquilinato'),
    ('Cuarto(s) en otro tipo de estructura', 'Cuarto(s) en otro tipo de estructura'),
    ('Vivienda Indígena', 'Vivienda Indígena'),
    ('Otro', 'Otro')   
]




class hijos(models.Model):
    _name = 'hijos'
    _description = "hijos"
    _inherit = 'hr.applicant'

    


    name_hijo = fields.Char(required=True)
    fecha_nac=fields.Date(string="Fecha de Nacimiento")
  


class Todoo(models.Model):
    _inherit = 'hr.applicant'
   
   
    #campos del grupo 1 page informacion general
    name1 = fields.Char(string="Primer Apellido")
    name2 = fields.Char(string="Segundo Apellido")
    name3 = fields.Char(string="Primer Nombre")
    name4 = fields.Char(string="Segundo Nombre")
    tratamiento = fields.Selection([('DRA.', 'DRA.'),('SRA.', 'SRA.'),('SRTA.', 'SRTA.'), ('ING.', 'ING.')])
    name5 = fields.Many2one('res.country')
    nit = fields.Char(string='NIT', size=11)
    tipod=fields.Selection([('N.U.I.P', 'N.U.I.P'),('Cédula de Ciudadania', 'Cédula de Ciudadania'),('Cédula de Extranjería', 'Cédula de Extranjería'), ('Tarjeta de Identidad', 'Tarjeta de Identidad'),('Pasaporte','Pasaporte'),('NIT','NIT'),('Registro Civil','Registro Civil'),('Pasado Judicial','Pasado Judicial'),('Libreta Militar','Libreta Militar'),('Licencia de Conducción','Licencia de Conducción'),('Visa','Visa'),('Antecedentes Disciplinarios','Antecedentes Disciplinarios'),('RUT','RUT')])
    ide=fields.Char(string="Número de Identificación")
    cide=fields.Char(string="Confirmar Número de Identificación")
    lugar_expedicion=fields.Many2one('ciudades')

    #Campos de Dirección. tipo DIAN
    field_1 = fields.Selection(av)
    field_2 = fields.Integer(required=True)
    field_3 = fields.Selection(alphabet)
    field_4 = fields.Selection(dire)
    field_5 = fields.Integer(required=True)
    field_6 = fields.Selection(alphabet)
    field_7 = fields.Selection(dire)
    field_8 = fields.Integer(required=True)
    field_9 = fields.Selection(dire)
    field_10 = fields.Char()
    field_11 = fields.Char(required=True)
    field_12 = fields.Char()
    street = fields.Char()

    #campos grupo 2 de la page informacion general
    name13 = fields.Char(string="Nombre Completo")    
    pais= fields.Many2one('res.country')
    namef = fields.Date(string="Fecha de Nacimiento")
    conf=fields.Date(string="Confirmar Fecha de Nacimiento")    
    dep=fields.Many2one('res.country.state')
    city=fields.Char(string="Ciudad")
    barrio=fields.Char(string="Barrio de Residencia")  

    
    #tallas, pantalon, camisa, saco, zapatos
    tallap=fields.Selection([('XS', 'XS'),('S', 'S'),('M', 'M'), ('L', 'L'),('X','X'),('XL','XL'),('XXL','XXL')])
    tallac=fields.Selection([('XS', 'XS'),('S', 'S'),('M', 'M'), ('L', 'L'),('X','X'),('XL','XL'),('XXL','XXL')])
    tallas=fields.Selection([('XS', 'XS'),('S', 'S'),('M', 'M'), ('L', 'L'),('X','X'),('XL','XL'),('XXL','XXL')])
    tallaz=fields.Selection(tallazapatos)
     
    #telegono,celular,correo,confirmar correo, idioma nativo, grupo sanguineo, genero. 
    tel=fields.Char(string="Télefono")
    cel=fields.Char(string="Celular")
    correo=fields.Char(string="Correo")
    ccorreo=fields.Char(string="Confirmar Correo")
    idioma=fields.Many2one('res.lang')
    grupo_san=fields.Selection(grupo_san)
    genero=fields.Selection([('Masculino', 'Masculino'),('Femenino', 'Femenino'),('Indefinido', 'Indefinido')])

    #GRUPO: INFORMACION DE VIVIENDA
    tipo_vivienda=fields.Selection(tipo_vivienda)
    cual_tipo_vivienda=fields.Char()
    carac_vivienda=fields.Char(string="Características de la Vivienda")
    zona_vivienda=fields.Char(string="Zona de Vivienda")
    ser_energia_elec=fields.Selection([('Si', 'Si'),('No', 'No')])
    alcantarilla=fields.Selection([('Si', 'Si'),('No', 'No')])
    acc=fields.Selection([('Si', 'Si'),('No', 'No')])

    #GRUPO: INFORMACION DE VIVIENDA2
    basura=fields.Selection([('Si', 'Si'),('No', 'No')])
    etnico=fields.Selection([('Mestizo', 'Mestizo'),('Blanco', 'Blanco'),('Afrocolombiano', 'Afrocolombiano'),('Indigena','Indigena'),('Gitano','Gitano')])
    estrato=fields.Selection([('1', '1'),('2', '2'),('3', '3'),('4','4'),('5','5'),('6','6')])
    gt=fields.Selection([('Si', 'Si'),('No', 'No')])

   
    



    nombre_completo=fields.Char(string="Nombre Completo")
    tel_contacto=fields.Char(string="Télefono")
    Parentesco=fields.Char(string="Parentesco")
    direccion_contacto=fields.Char(string="Dirección del contacto")


    re=fields.Selection([('Si', 'Si'),('No', 'No')])
    pe_eco=fields.Selection([('Si', 'Si'),('No', 'No')])
    cab_familia=fields.Selection([('Si', 'Si'),('No', 'No')])
  

    mascotas=fields.Integer(string="Numero de Mascotas")
    tipo_mascotas=fields.Char(string="Tipo de Mascotas")
    lic_conducir=fields.Selection([('Si', 'Si'),('No', 'No')])
    tipo_lic_conducir=fields.Selection([('A1', 'A1'),('A2', 'A2'),('B1', 'B1'),('B2','B2'),('B3','B3'),('C1', 'C1'),('C2','C2'),('C3','C3')])
    medio_transporte=fields.Char(string="Medio de Transporte")
    medio_transporte_sec=fields.Char("Medio de Transporte Secundario")
    Horas_trabajo=fields.Integer(string="Horas para llegar al Trabajo")
    estudia_actualmente=fields.Selection([('Si', 'Si'),('No', 'No')])
    año_graduacion=fields.Date(string="Año de Graduación")
    escolaridad=fields.Selection([('Primaria', 'Primaria'),('Bachiller', 'Bachiller'),('Curso o Seminario', 'Curso o Seminario'),('Técnica','Técnica'),('Tecnológica','Tecnológica'),('Universitaria', 'Universitaria'),('Especialización', 'Especialización'),('Maestría','Maestría'),('Doctorado','Doctorado')])
    estado_civil=fields.Selection([('Soltero/a', 'Soltero/a'),('Casado/a', 'Casado/a'),('Divorciado/a', 'Divorciado/a'),('Unión Libre','Unión Libre'),('Viudo/a','Viudo/a')])

    #campos conyugue
    primer_apellido_conyugue=fields.Char(string="Primer Apellido del Cónyugue")
    segundo_apellido_conyugue=fields.Char(string="Segungo Apellido del Cónyugue")
    primer_nombre_conyugue=fields.Char(string="Primer Nombre del Cónyugue")
    segundo_nombre_conyugue=fields.Char(string="Segundo Nombre del Cónyugue")
    escolaridad_conyugue=fields.Selection([('Primaria', 'Primaria'),('Bachiller', 'Bachiller'),('Curso o Seminario', 'Curso o Seminario'),('Técnica','Técnica'),('Tecnológica','Tecnológica'),('Universitaria', 'Universitaria'),('Especialización', 'Especialización'),('Maestría','Maestría'),('Doctorado','Doctorado')])
    genero_conyugue=fields.Selection([('Masculino', 'Masculino'),('Femenino', 'Femenino'),('Indefinido', 'Indefinido')])
    lugar_nacimiento_conyugue=fields.Char(string="Lugar de Nacimiento del Cónyugue")
    pais_nacimiento_conyugue=fields.Many2one('res.country')

    #campos relacionados traidos de la requisición
    requisicion=fields.Many2one('requisiciones')
    emp_aplica=fields.Char(string='Cargo del Solicitante', related='requisicion.emp.name')
    cargo_aplica=fields.Char(string="Cargo al que Aplica", related="requisicion.cargo_solicitado.name")
    jefe=fields.Char(string="Jefe Inmediato", related="requisicion.jefe_inmediato.name")
   


     

    Compañia=fields.Many2one('res.company')

    otro_idioma=fields.Selection([('EN Ingles', 'EN Ingles'),('ES Español', 'ES Español'),('FR Francés', 'FR Francés'),('IT Italiano','IT Italiano')])
    porcent_dominio=fields.Integer(string="Porcentaje de Dominio")
    po=fields.Integer( related="porcent_dominio") 

    miedos=fields.Char(string="Miedos o Fobias")
    hobby=fields.Char(string="Hobby")
    tiene_enfermedad=fields.Char(string="Tiene alguna enfermedad Importante")
    toma_medicamneto=fields.Char(string="Toma algun Medicamento")
    tiene_alergia=fields.Char(string="Tiene alguna Alergia")


    fotocopia_cedula=fields.Binary(string="Fotocopia de la Cédula")
    cer_estudio=fields.Binary(string="Certificados de Estudio")

    certi_laborales=fields.Binary()
    hv=fields.Binary()

    aceptacion_condiciones=fields.Binary()
    libreta_militar=fields.Binary()
    refrecnias_personales=fields.Binary()
    verificacion_referencias=fields.Binary()
    
    certificado_cuenta_bancaria=fields.Binary()
    antecedentes_disciplinarios=fields.Binary()
    validacion_antecedentes=fields.Binary()

    entrevista_jefe_inmediato=fields.Binary()
    fotografias=fields.Binary()
    Validación_Sarlaft=fields.Binary()
    TGS_Solidarios=fields.Binary()

    estudio_seguridad=fields.Binary()
    examendes_medicos=fields.Binary()
    poliza=fields.Binary()
    autorizacion_uso_correo=fields.Binary()

    licencia_conducir=fields.Binary()
    carta_propiedad_vehiculo=fields.Binary()
    autorizacion_propietario=fields.Binary()

    cer_runt=fields.Binary()
    seguro_obligatorio_vigente=fields.Binary()
    revision_tecnico_mecanica=fields.Binary()

    formacion=fields.Boolean()
    experiencia=fields.Boolean()
    habilidades=fields.Boolean()
    educacion=fields.Boolean()

    fecha_compromiso=fields.Date()
    fecha_vencimiento=fields.Date()

    plan_accion=fields.Text()



    

     
    @api.constrains('nit')
    def _check_nit_size(self):
        pattern = "^\+?[0-9]*$" 
        for record in self:
            if record.nit and re.match(pattern, record.nit) is None:
                raise ValidationError(("NIT debe ser numerico"))

    

    @api.onchange('field_1', 'field_2', 'field_3', 'field_4', 'field_5',
                  'field_6', 'field_7', 'field_8', 'field_9', 'field_10',
                  'field_11', 'field_12')
    def _onchange_street(self):
        self.street = "%s %s  %s %s %s %s %s %s %s %s %s %s" % (
            self.field_1 if self.field_1 else "",
            str(self.field_2),
            str(self.field_3 if self.field_3 else ""),
            self.field_4 if self.field_4 else "",
            str(self.field_5),
            str(self.field_6 if self.field_6 else ""),
            self.field_7 if self.field_7 else "",
            str(self.field_8),
            self.field_9 if self.field_9 else "",
            self.field_10 if self.field_10 else "",
            self.field_11 if self.field_11 else "",
            self.field_12 if self.field_12 else "") 


  