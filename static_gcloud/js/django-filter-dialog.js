document.addEventListener("click", function (event) {
    const trigger = event.target.closest("[data-filter-dialog]");
    if (!trigger || !window.bootbox) {
        return;
    }

    const formContainer = document.getElementById(trigger.dataset.filterDialog);
    const form = formContainer && formContainer.querySelector("form");
    if (!form) {
        return;
    }

    const dialog = window.bootbox.dialog({
        title: "Filtros",
        message: $(form),
        closeButton: false,
        buttons: {
            close: {
                label: "Fechar",
                className: "btn-outline-secondary"
            },
            clear: {
                label: "Limpar",
                className: "btn-outline-secondary",
                callback: function () {
                    window.location.assign(window.location.pathname);
                }
            },
            filter: {
                label: "Filtrar",
                className: "btn-primary",
                callback: function () {
                    form.requestSubmit();
                    return false;
                }
            }
        }
    });

    dialog.on("hidden.bs.modal", function () {
        formContainer.appendChild(form);
    });
});