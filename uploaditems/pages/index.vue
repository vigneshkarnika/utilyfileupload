<template>
<div class="container">
    <input type="file" @change="imagesPicked" ref="file" style="display: none" multiple>
        <a-button @click="$refs.file.click()" type="primary" shape="round" icon="upload" >convert ai,eps,png,tiff to jpg</a-button>

    <!-- <button @click="$refs.file.click()">convert ai,eps,png,tiff to jpg</button> -->
</div>
</template>

<script>
var async = require("async");

export default {
    data() {
        return {};
    },
    methods: {
        imagesPicked(e) {
            var that = this;

            async.eachLimit(e.target.files, 1, async function (file, cb) {
                console.log("calling:");
                var formData = new FormData();
                formData.append("file", file);
                try {
                    await new Promise((res, reject) => {
                        that.$axios({
                            url: `/utility/upload`,
                            method: 'POST',
                            data: formData,
                            responseType: 'blob', // important
                            headers: {
                                "Content-Type": "multipart/form-data"
                            },
                        }).then((response) => {
                            const url = window.URL.createObjectURL(new Blob([response.data]));
                            const link = document.createElement('a');
                            link.href = url;
                            link.setAttribute('download', file.name + ".jpg");
                            document.body.appendChild(link);
                            link.click();
                            res(true)
                        }).catch(err => {
                            reject(err)
                        })
                    })

                } catch (err) {
                    console.log(err)
                } finally {
                    cb()
                }

            })

        }
    },
}
</script>

<style>
.container {
    margin: 0 auto;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.title {
    font-family:
        'Quicksand',
        'Source Sans Pro',
        -apple-system,
        BlinkMacSystemFont,
        'Segoe UI',
        Roboto,
        'Helvetica Neue',
        Arial,
        sans-serif;
    display: block;
    font-weight: 300;
    font-size: 100px;
    color: #35495e;
    letter-spacing: 1px;
}

.subtitle {
    font-weight: 300;
    font-size: 42px;
    color: #526488;
    word-spacing: 5px;
    padding-bottom: 15px;
}

.links {
    padding-top: 15px;
}
</style>
