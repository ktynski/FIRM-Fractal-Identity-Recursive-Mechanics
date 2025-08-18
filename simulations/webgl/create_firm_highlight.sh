#!/bin/bash
# FSCTF Klein Bottle Pattern Analysis Video

echo "🔬 Creating FSCTF Klein Bottle Pattern Analysis..."
echo "📚 Documentary-style exploration of mathematical self-reference patterns"
echo "✂️  Cropping visualization (removing UI elements)"
echo ""

echo "Step 1/5: Extracting and cropping key transition segments..."

echo "Extracting transition 1/8 (Introduction)..."
ffmpeg -y -i screencap.mov -ss 200 -t 15 \
    -vf "crop=2408:1834:927:0" \
    -c:v libx264 -crf 18 -c:a aac -b:a 128k \
    video_segment_00.mp4

echo "Extracting transition 2/8 (Pattern Recognition)..."
ffmpeg -y -i screencap.mov -ss 220 -t 15 \
    -vf "crop=2408:1834:927:0" \
    -c:v libx264 -crf 18 -c:a aac -b:a 128k \
    video_segment_01.mp4

echo "Extracting transition 3/8 (Scale Emergence)..."
ffmpeg -y -i screencap.mov -ss 390 -t 20 \
    -vf "crop=2408:1834:927:0" \
    -c:v libx264 -crf 18 -c:a aac -b:a 128k \
    video_segment_02.mp4

echo "Extracting transition 4/8 (Hierarchical Integration)..."
ffmpeg -y -i screencap.mov -ss 440 -t 15 \
    -vf "crop=2408:1834:927:0" \
    -c:v libx264 -crf 18 -c:a aac -b:a 128k \
    video_segment_03.mp4

echo "Extracting transition 5/8 (Pure Information Processing)..."
ffmpeg -y -i screencap.mov -ss 510 -t 15 \
    -vf "crop=2408:1834:927:0" \
    -c:v libx264 -crf 18 -c:a aac -b:a 128k \
    video_segment_04.mp4

echo "Extracting transition 6/8 (Maximum Complexity)..."
ffmpeg -y -i screencap.mov -ss 640 -t 20 \
    -vf "crop=2408:1834:927:0" \
    -c:v libx264 -crf 18 -c:a aac -b:a 128k \
    video_segment_05.mp4

echo "Extracting transition 7/8 (Abstract Transcendence)..."
ffmpeg -y -i screencap.mov -ss 750 -t 15 \
    -vf "crop=2408:1834:927:0" \
    -c:v libx264 -crf 18 -c:a aac -b:a 128k \
    video_segment_06.mp4

echo "Extracting transition 8/8 (Complete Understanding)..."
ffmpeg -y -i screencap.mov -ss 820 -t 25 \
    -vf "crop=2408:1834:927:0" \
    -c:v libx264 -crf 18 -c:a aac -b:a 128k \
    video_segment_07.mp4

echo "Step 2/5: Concatenating Klein bottle transition segments..."
echo -e "file 'video_segment_00.mp4'\nfile 'video_segment_01.mp4'\nfile 'video_segment_02.mp4'\nfile 'video_segment_03.mp4'\nfile 'video_segment_04.mp4'\nfile 'video_segment_05.mp4'\nfile 'video_segment_06.mp4'\nfile 'video_segment_07.mp4'" > video_segments.txt
ffmpeg -y -f concat -safe 0 -i video_segments.txt -c copy temp_video.mp4

echo "Step 3/5: Concatenating documentary narration..."
echo -e "file 'voiceover_00.mp3'\nfile 'voiceover_01.mp3'\nfile 'voiceover_02.mp3'\nfile 'voiceover_03.mp3'\nfile 'voiceover_04.mp3'\nfile 'voiceover_05.mp3'\nfile 'voiceover_06.mp3'\nfile 'voiceover_07.mp3'" > audio_segments.txt
ffmpeg -y -f concat -safe 0 -i audio_segments.txt -c copy temp_audio.mp3

echo "Step 4/5: Combining visualization with documentary narration..."
ffmpeg -y -i temp_video.mp4 -i temp_audio.mp3 \
    -c:v copy -c:a aac -b:a 128k \
    -map 0:v:0 -map 1:a:0 \
    fsctf_firm_theoretical_highlight.mp4

echo "Step 5/5: Cleaning up temporary files..."
rm temp_video.mp4 temp_audio.mp3 video_segments.txt audio_segments.txt
rm video_segment_*.mp4 voiceover_*.mp3

echo ""
echo "✅ Klein bottle pattern analysis created: fsctf_firm_theoretical_highlight.mp4"
echo "📊 Mathematical Pattern Documentation:"
echo "   • Duration: ~2m20s covering 8 Klein bottle transitions"
echo "   • Natural documentary presentation style"
echo "   • Pure visualization (UI removed)"
echo "   • Accessible scientific explanation"
echo ""
echo "🎯 Applications:"
echo "   • Mathematical pattern research"
echo "   • Topology and recursion studies"
echo "   • Educational mathematics content"
echo "   • Scientific communication examples"

