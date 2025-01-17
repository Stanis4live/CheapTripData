import asyncio
from datetime import datetime, timedelta

from socials.fb import add_task_facebook
from utils.config import config
from utils.methods import start_func, get_last_post_date


async def main():
    # Facebook
    page_name = 'CheapTrip. Pay less, visit more.'
    facebook = {'page_name': page_name, 'acc_token': config.fb_token.get_secret_value(), 'task': add_task_facebook}

    # Fill In this fields
    social = facebook
    posting_interval = timedelta(hours=1)

    data_folder_path = 'files/posts/city_attractions/ru'
    posting_start_date = get_last_post_date('Facebook') + posting_interval

    await start_func(data_folder_path=data_folder_path, start_date=posting_start_date, interval=posting_interval,
                     **social)


if __name__ == "__main__":
    asyncio.run(main())
