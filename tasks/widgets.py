from django.forms import widgets


class PickADateDateWidget(widgets.Input):
    class Media:
        css = {
            'all': ('pickadate/themes/default.css', 'pickadate/themes/default.date.css')
        }
        js = ('https://code.jquery.com/jquery-3.2.1.js', 'pickadate/picker.js', 'pickadate/picker.date.js')

    template_name = 'widgets/pickadate.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['options'] = {'format': "yyyy-mm-dd"}
        return context
