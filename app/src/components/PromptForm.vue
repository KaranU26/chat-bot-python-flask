<template>
    <div class="container mt-5">
        <form @submit.prevent="submitPrompt">
            <div class="mb-3">
                <label for="promptText" class="form-label">Enter your prompt:</label>
                <input type="text" class="form-control prompt" id="promptText" v-model="prompt" :disabled="loading"/>
            </div>
            <button type="submit" class="btn btn-primary" :disabled="loading">Submit</button>
        </form>
        <br />
        <div v-if="response" v-html="formattedResponse"></div>

        <div v-if="loading" class="spinner-border" role="status">
            <span class="visually-hidden">Loading Response...</span>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { marked } from 'marked';

export default {
    data() {
        return {
            prompt: '',
            response: undefined,
            loading: false
        };
    },
    computed: {
        formattedResponse() {
            return this.response ? marked(this.response) : '';
        }
    },
    methods: {
        async submitPrompt() {
            try {
                this.loading = true;
                const res = await axios.post('http://localhost:5000/prompt', {
                    prompt: this.prompt
                });

                this.response = res.data.response;
            } catch (error) {
                console.error(error);
            } finally {
                this.prompt = '';
                this.loading = false;
            }
        }
    }
}
</script>

<style scoped>
.spinner-border {
    display: inline-block;
    width: 2rem;
    height: 2rem;
    vertical-align: text-bottom;
    border: 0.25em solid currentColor;
    border-right-color: transparent;
    border-radius: 50%;
    animation: spinner-border .75s linear infinite;
}

@keyframes spinner-border {
    to { transform: rotate(360deg); }
}

.visually-hidden {
    position: absolute;
    width: 1px;
    height: 1px;
    margin: -1px;
    padding: 0;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    border: 0;
}

.form-control {
    width: 100%;
    display: inline;
}
</style>