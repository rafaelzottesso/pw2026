(function ($) {
    'use strict';

    function mascaraTelefone(valor, evento, campo, opcoes) {
        var quantidadeDigitos = valor.replace(/\D/g, '').length;
        var mascara = quantidadeDigitos > 10
            ? '(00) 00000-0000'
            : '(00) 0000-00009';

        $(campo).mask(mascara, opcoes);
    }

    $(function () {
        $('input[name]').each(function () {
            var campo = $(this);
            var identificadores = (campo.attr('name') + ' ' + (campo.attr('id') || '')).toLowerCase();

            if (identificadores.indexOf('cpf') !== -1) {
                campo.mask('000.000.000-00');
            } else if (identificadores.indexOf('cnpj') !== -1) {
                campo.mask('00.000.000/0000-00');
            } else if (identificadores.indexOf('cep') !== -1) {
                campo.mask('00000-000');
            } else if (
                identificadores.indexOf('telefone') !== -1 ||
                identificadores.indexOf('celular') !== -1 ||
                identificadores.indexOf('whatsapp') !== -1
            ) {
                campo.mask('(00) 0000-00009', {
                    onKeyPress: mascaraTelefone
                });
            }
        });
    });
})(jQuery);