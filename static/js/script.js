$(document).ready(function () {
    initTable()
    fundoRed()
    initDateRangePicker()
})
// Altera a cor de fundo da célula de acordo com a condição:
function fundoRed() {
    $('#tabela tbody tr').each(function (i) {
        tr = $(this);
        tr.children('td').removeClass('fundoRed');
        valor = tr.children('td:eq(4)').html();
        if (valor > 3) {
            tr.children('td:eq(4)').addClass('fundoRed');
        }
    })
}
// Inicializa a DataTable:
function initTable() {
    $('#tabela').DataTable({
        paging: false,
        info: false,
        searching: true,
        language: {
            "search": "PESQUISAR:",
            "zeroRecords": "NENHUM REGISTRO ENCONTRADO",
        },

    });
}
// Processa o Date Range Picker:
function initDateRangePicker() {
    $('input[name="daterange"]').daterangepicker();
    var date_range = $('#selector').val();
    var dates = date_range.split(" - ");
    var start = dates[0];
    var end = dates[1];
    filter(start, end);
    $('#selector').on('apply.daterangepicker', function (ev, picker) {
        var date_range = $('#selector').val();
        var dates = date_range.split(" - ");
        var start = dates[0];
        var end = dates[1];
        filter(start, end);
    });
}
// Realiza a filtragem por data:
function filter(dataInicial, dataFinal) {
    var date1 = dataInicial;
    var date2 = dataFinal;
    var parts1 = date1.split('/');
    var parts2 = date2.split('/');
    let dataDe = new Date(parts1[2], parts1[1] - 1, parts1[0]);
    let dataAte = new Date(parts2[2], parts2[1] - 1, parts2[0]);
    $('#tabela tbody tr').each(function (i) {
        tr = $(this);
        dataCompra = tr.children('td:eq(2)').html();
        var parts3 = dataCompra.split('/');
        let data = new Date(parts3[2], parts3[1] - 1, parts3[0]);
        if (data.getTime() >= dataDe.getTime() && data.getTime() <= dataAte.getTime()) {
            $(this).removeClass('hide')
        } else {
            $(this).addClass('hide')
        }
    });
}