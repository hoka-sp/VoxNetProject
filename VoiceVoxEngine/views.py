from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from .voicevox_service import CreateWavBytes  # 音声生成クラスをインポート


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            processor = CreateWavBytes()
            file_name = processor.create_wav_file(post.text, speaker_id=1, output_path='media/audio')
            post.audio_file = f'audio/{file_name}.wav'
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})
