// Inicializa as tabelas de listagem com uma configuração única para o projeto.
$(document).ready(function () {
  $('table.table-datatable').each(function () {
    $(this).DataTable({
      paging: false,
      info: false,
      lengthChange: false,
      order: [],
      layout: {
        topStart: {
          buttons: [
            {
              extend: 'pdfHtml5',
              text: 'PDF',
              orientation: 'landscape',
              pageSize: 'A4',
              exportOptions: { columns: ':not([data-orderable="false"])' }
            },
            {
              extend: 'excelHtml5',
              text: 'Excel',
              exportOptions: { columns: ':not([data-orderable="false"])' }
            },
            {
              extend: 'csvHtml5',
              text: 'CSV',
              exportOptions: { columns: ':not([data-orderable="false"])' }
            }
          ]
        },
        topEnd: 'search'
      },
      language: { url: 'https://cdn.datatables.net/plug-ins/2.1.8/i18n/pt-BR.json' }
    });
  });
});