$(document).ready(function () {
    const $form = $('#chatForm');
    const $input = $('#userQuery');
    const $historyContainer = $('#chatHistory');
    const $loading = $('#loadingIndicator');
    const $sendBtn = $('#sendBtn');
    const $emptyState = $('#emptyState');
    const $clearBtn = $('#clearHistoryBtn');

    $form.on('submit', function (e) {
        e.preventDefault();
        const query = $input.val().trim();
        if (!query) return;

        $input.prop('disabled', true);
        $sendBtn.prop('disabled', true);
        $loading.fadeIn();
        $emptyState.hide();

        $.ajax({
            url: '/api/ask-ai',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ query: query }),
            success: function (response) {
                addMessageToHistory(query, response.answer, response.success);
            },
            error: function () {
                addMessageToHistory(query, "Something went wrong communicating with the server. Please try again", false);
            },
            complete: function () {
                $input.val('').prop('disabled', false).focus();
                $sendBtn.prop('disabled', false);
                $loading.hide();
            }
        });
    });

    function addMessageToHistory(question, answer, isSuccess) {
        const cardHtml = `
            <div class="card border-0 shadow-sm">
                <div class="card-body">
                    <div class="mb-3">
                        <div>
                            <h6 class="fw-bold mb-1">You</h6>
                            <p class="mb-0 text-dark">${question}</p>
                        </div>
                    </div>
                    <hr class="my-2 opacity-25">
                    <div class="mt-3">
                        <div>
                            <h6 class="fw-bold mb-1 text-primary">AI</h6>
                            <div class="text-dark ${isSuccess ? '' : 'text-danger'}">
                                ${formatAnswer(answer)}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

        $historyContainer.prepend(cardHtml);
    }

    $clearBtn.on('click', function () {
        if (confirm('Are you sure you want to clear the chat history?')) {
            $historyContainer.empty();
            $emptyState.fadeIn();
        }
    });

    function formatAnswer(text) {
        return $('<div>').text(text).html().replace(/\n/g, '<br>');
    }
});