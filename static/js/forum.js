 $(document).ready(function () {
            tinymce.init({
                selector: '#reply',
                plugins: 'fullscreen',
                toolbar: [
                    'fullscreen | undo redo | styles | bold italic | alignleft aligncenter alignright'
                ],
                height: '280',
                toolbar_location: 'top',
                toolbar_mode: 'wrap',
                menubar: false,
                browser_spellcheck: true,
                contextmenu: false,
                newline_behavior: 'linebreak',
                InsertLineBreak: true,
            });

            $('#createForm').submit(function (e) {
                let rp = $('#reply').val();
                let ForumId = $('#forum').data('id');
                let rp_ = $("#invalid-msg");

                $(rp).serialize();
                if (rp === '') {
                    rp_.show("#invalid-msg");
                    return false
                }
                e.preventDefault()
                e.stopPropagation()


                $.ajax({
                    type: 'POST',
                    url: '{% url "forum:create_disc" %}',
                    data: {
                        rp: rp,
                        ForumId: ForumId,
                        csrfmiddlewaretoken: '{{csrf_token}}',
                        action: 'POST',
                        dataType: 'json',
                    },
                    success: function (json) {
                        console.log(json)
                        $('#successMsg').show().delay(5000).fadeOut();

                    },
                    complete:
                        function (json) {
                            console.log(json)
                            setTimeout(function () {
                                $("#body_refresh").load("#body_refresh")
                            }, 1000);
                        },

                    error: function (xhr, json, thrownError) {
                        console.log(json);
                        if (xhr.status === 404 || xhr.status === 500) {
                            $('#errorMsg').show().delay(5000).fadeOut();
                        }
                    },

                });

            });

}); /// Document ready