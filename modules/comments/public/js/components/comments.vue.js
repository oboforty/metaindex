export const template = `<div v-if="meta_id">
    <div v-if="user && (user.curator || user.admin)">
        <div class="input-group mb-3">
            <textarea v-model="input_text" @keyup.enter="onSendComment" class="form-control" placeholder="Add comment..."></textarea>

            <div class="input-group-prepend">
                <button @click="onSendComment" class="btn bg-info text-white" type="button">Send</button>
            </div>
          </div>
    </div>


    <div class="media comment-box mt-2" v-for="comment in comments">
        <div class="media-left">
            <a href="#">
                <img class="img-responsive user-photo" src="https://ssl.gstatic.com/accounts/ui/avatar_2x.png">
            </a>
        </div>
        <div class="media-body">
            <div class="media-heading bg-info text-white p-1 pl-2">
                <span class="ra ra-house" v-if="comment.author && comment.author.admin"></span> 
                <span class="ra ra-id-card" v-else-if="comment.author && comment.author.curator"></span> 
                {{ comment.author.username }}
            </div>
            <p class="p-2">{{ comment.content }}</p>
        </div>
    </div>



</div>`;