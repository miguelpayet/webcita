from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from app.common import utils
from app.common.seccion_instalacion import fotos_instalacion_detalle
from app.models.SeccionInstalacion import FotoInstalacion
from app.models.SeccionInstalacion import TextoFotoInstalacion


class InstalacionDetalle(TemplateView):

    def get(self, request, *args, **kwargs):
        idfoto = None
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
        return render(request, 'app/seccion_instalacion_detalle.html', {'imagen': dict_padre})
        # return HttpResponse('<h1>idfoto %s</h1>' % idfoto, content_type='application/html')

    def nada(self):
        txt = None
        # try:
        #     txt = foto.textofotoinstalacion_set.get(idioma__codigo=cur_language)
        # except TextoFotoInstalacion.DoesNotExist:
        #     raise Exception("no existe texto para foto %s en instalación %s" % (foto.imagen, seccion.nombre))
        # arr_detalle = fotos_instalacion_detalle(foto.idfoto)
        # dict_hijo = {'active': active, 'fotos': arr_detalle, 'texto': txt.texto}
        # arr_fotos[pos] = {'active': active, 'id': foto.idfoto, 'imagen': foto.imagen, 'texto': txt.titulo, 'hijo': dict_hijo}
        # active = False
        # if (pos + 1) == total:
        #     arr_filas.append({'active': tiene_foto_activa(arr_fotos), 'fotos': arr_fotos})
        # pos += 1
        # if pos < total:  # añadir última fila
        #     arr_filas.append(arr_filas)
        # return arr_filas
