import sys
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter, JSONFormatter


def list_transcripts(video_id):
    # retrieve the available transcripts
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    for transcript in transcript_list:

        # the Transcript object provides metadata properties
        print(
            transcript.video_id,
            transcript.language,
            transcript.language_code,
            # whether it has been manually created or generated by YouTube
            transcript.is_generated,
            # whether this transcript can be translated or not
            transcript.is_translatable,
            # a list of languages the transcript can be translated to
            transcript.translation_languages,
        )

        # fetch the actual transcript data
        # print(transcript.fetch())

        # translating the transcript will return another transcript object
        # print(transcript.translate('en').fetch())

    # you can also directly filter for the language you are looking for, using the transcript list
    # transcript = transcript_list.find_transcript(['de', 'en'])
    # transcript = transcript_list.find_transcript(['en'])

    # or just filter for manually created transcripts
    # transcript = transcript_list.find_manually_created_transcript(['de', 'en'])

    # or automatically generated ones
    # transcript = transcript_list.find_generated_transcript(['de', 'en'])


def write_json_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = JSONFormatter()
    json_formatted = formatter.format_transcript(transcript)

    with open(f'youtube_transcript_{video_id}.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_formatted)


def write_text_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = TextFormatter()
    text_formatted = formatter.format_transcript(transcript)

    with open(f'youtube_transcript_{video_id}.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(text_formatted)
        print(f'Wrote transcript to youtube_transcript_{video_id}.txt')


def main():
    video_id = sys.argv[1]
    write_text_transcript(video_id)


if __name__ == '__main__':
    main()
