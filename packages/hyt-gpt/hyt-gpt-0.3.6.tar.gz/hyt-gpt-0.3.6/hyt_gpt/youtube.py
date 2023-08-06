from typing import Dict, Any, List, Union, Tuple
from .gpt import seg_transcript, chat_gpt
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
import traceback
import logging
import re

headers = {
    "authority": "api.youtube.com",
    "accept": "application/json, text/plain, */*",
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
}


class HytGpt:
    def __init__(self, gpt_key: str, prompt: str):
        self.gpt_key = gpt_key
        self.prompt = prompt

    def summary(self, ylink: str) -> Dict[str, str]:
        if not self.is_valid_youtube_url(ylink):
            return {
                "status": "failed",
                "url": ylink,
                "subtitles": [],
                "summaries": "Invalid youtube url",
            }
        subtitles, language = self.__youtube_subtitle(ylink)
        if not subtitles:
            return {
                "status": "failed",
                "url": ylink,
                "subtitles": subtitles,
                "summaries": "Subtitle retrieval failed",
            }

        seged_text = seg_transcript(subtitles)
        print(len(HytGpt.parse_text_from_start_duration(subtitles)))
        summaried_text = ""
        # i = 1

        # for entry in seged_text:
        #     try:
        #         response = chat_gpt(
        #             self.gpt_key, self.prompt.format(language=language), entry
        #         )
        #         print(f"Completed the {str(i)} part summary")
        #         i += 1
        #     except Exception as e:
        #         print(f"Exception occurred: {str(e)}")
        #         traceback.print_exc()
        #         response = "Summary failed"
        #     summaried_text += response + "\n"
        response_data = {
            "status": "success",
            "url": ylink,
            "subtitles": subtitles,
            "summaries": summaried_text,
        }
        return response_data

    @staticmethod
    def is_valid_youtube_url(url):
        # Regular expression pattern for YouTube URLs
        youtube_url_pattern = re.compile(
            r"(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+"
        )

        # Check if the URL matches the pattern
        if youtube_url_pattern.match(url):
            return True
        else:
            return False

    @staticmethod
    def get_youtube_id(url: str) -> str:
        youtube_id_match = re.search(r"(?<=v=)[^&#]+", url)
        youtube_id_match = youtube_id_match or re.search(r"(?<=be/)[^&#]+", url)
        return youtube_id_match.group(0) if youtube_id_match else None

    @staticmethod
    def build_youtube_url(youtube_id: str) -> str:
        return f"https://www.youtube.com/watch?v={youtube_id}"

    @staticmethod
    def get_timestamp_diff(start_time, end_time):
        start_time = datetime.strptime(start_time, "%H:%M:%S.%f")
        end_time = datetime.strptime(end_time, "%H:%M:%S.%f")
        diff = (end_time - start_time).total_seconds()
        return diff

    @staticmethod
    def should_concatenate(segment1, segment2, max_time_difference=1.1): # seconds
        current_end_time = segment1['start'] + segment1['duration']
        next_start_time = segment2['start']
        is_close = current_end_time + max_time_difference > next_start_time
        no_punctuation = not segment1['text'].strip().endswith(('.', '?', '!'))
        return is_close and no_punctuation

    @staticmethod    
    def parse_text_from_start_duration(subtitles: List[Dict[str, str]]) -> List[str]:
        combined_texts = []
        current_text = subtitles[0]['text']
        current_segment = subtitles[0]

        for i in range(1, len(subtitles)):
            next_segment = subtitles[i]
            
            if HytGpt.should_concatenate(current_segment, next_segment):
                current_text += " " + next_segment['text']
            else:
                combined_texts.append(current_text)
                current_text = next_segment['text']

            current_segment = next_segment

        combined_texts.append(current_text)
        return combined_texts


    def __youtube_subtitle(
        self, url: str
    ) -> Tuple[Union[List[Dict[str, str]], None], str]:
        video_id = self.get_youtube_id(url)
        list = YouTubeTranscriptApi.list_transcripts(video_id)
        logging.debug(list)
        
        for transcript in list:
            if transcript.language_code in ["en", "zh", "zh-Hans", "zh-Hant"]:
                return transcript.fetch(), transcript.language
        # if 'zh-Hans' in transicript.translation_languages:
        #     translated = transicript.translate('zh-Hans').fetch()
        #     return translated
        return None


"""
5/5/23: Older version

    def __youtube_player_list(self, yvid):
        url = f"https://www.youtube.com/watch?v={yvid}"
        response = requests.request("GET", url, headers=headers)
        return response.text


    def __get_text_from_url(self, url: str) -> str:
        response = requests.request("GET", url, headers=headers)
        return response.text


    def __parse_subtitles(self, subtitles) -> List[Dict[str, str]]:
        result = []
        subtitle_lines = subtitles.strip().split('\n')[3:]
        for i in range(0, len(subtitle_lines), 2):
            if ' --> ' not in subtitle_lines[i]:
                continue
            start, end = subtitle_lines[i].split(' --> ')
            text = subtitle_lines[i+1]

            result.append({
                'start': start,
                'end': end,
                'text': text
            })
        return result

    def __parse_requested_subtitles(self, requested_subtitles) -> List[Dict[str, str]]:
        result = []
        subtitle_lines = requested_subtitles.strip().split('\n')[3:]
        for i in range(0, len(subtitle_lines), 1):
            match_timestamp = re.match(r'(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})', subtitle_lines[i])
            if not match_timestamp:
                continue
            start = match_timestamp.group(1)
            end = match_timestamp.group(2)
            if self.get_timestamp_diff(start, end) <= 1:
                continue
            text = subtitle_lines[i+1]
            if not re.compile(r'[a-zA-Z]+').search(text):
                continue
            result.append({
                'start': start,
                'end': end,
                'text': text
            })
        return result        


    def __youtube_subtitle(self, url: str) -> List[Dict[str, str]]:
        # options for subtitle extraction
        options = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en', 'zh-Hans'],  # You can add more languages here
            'skip_download': True,  # We don't need to download the video
            'quiet': False  # Suppress console output
        }        
        with yt_dlp.YoutubeDL(options) as ydl:
            result = ydl.extract_info(url, download=False)

        # Extract the subtitles
        subtitles = []
        if 'subtitles' in result:
            print('Found subtitles.')
            for subtitle_list in result['subtitles'].values():
                for subtitle in subtitle_list:
                    if subtitle.get('ext') == 'vtt':
                        text = self.__get_text_from_url(subtitle.get('url'))
                        subtitles.extend(self.__parse_subtitles(text))
        
        if 'requested_subtitles' in result:
            print('Found requested subtitles.')
            requested_subtitles = result.get('requested_subtitles')
            if isinstance(requested_subtitles, dict) and 'en' in requested_subtitles:
                subtitle = requested_subtitles['en']
                if subtitle.get('ext') == 'vtt':
                    print('No subtitles found, fetching requested subtitles.')
                    text = self.__get_text_from_url(subtitle.get('url'))
                    subtitles.extend(self.__parse_requested_subtitles(text))
        print(f'Fetched {len(subtitles)} subtitles.')
        return subtitles


    def __to_subtitle_list(self, subtitles):
        results = []
        for subtitle in subtitles:
            if 'text' in subtitle:
                results.append(subtitle.get('text'))
        return results
"""
