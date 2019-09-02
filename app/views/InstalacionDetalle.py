from django.http import HttpResponse

from app.common import utils
from app.models.SeccionInstalacion import FotoInstalacion
from app.models.SeccionInstalacion import TextoFotoInstalacion
from app.secciones.seccion_instalacion import fotos_instalacion_detalle
from app.views.ViewBase import ViewBase


class InstalacionDetalle(ViewBase):

    def get_context_data(self, **kwargs):
        try:
            idfoto_param = self.request.GET.get('id')
            idfoto = int(idfoto_param)
        except Exception as ex:
            return HttpResponse(str(ex), status=400)
        cur_language = utils.get_language()
        try:
            foto = FotoInstalacion.objects.get(idfoto=idfoto)
        except FotoInstalacion.DoesNotExist:
            return HttpResponse("no existe foto con id %s" % idfoto, status=500)
        txt = None
        try:
            txt = foto.textofotoinstalacion_set.get(idioma__codigo=cur_language)
        except TextoFotoInstalacion.DoesNotExist:
            raise HttpResponse("no existe texto para foto %s" % foto.imagen, status=500)
        arr_detalle = fotos_instalacion_detalle(foto.idfoto)
        dict_hijo = {'active': True, 'fotos': arr_detalle, 'texto': txt.texto}
        dict_padre = {'hijo': dict_hijo}
        return {'imagen': dict_padre}
