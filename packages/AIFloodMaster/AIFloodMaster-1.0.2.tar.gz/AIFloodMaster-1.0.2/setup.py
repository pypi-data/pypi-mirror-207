import setuptools

with open("VERSION", "r") as info:
    Version = info.readline().strip()

setuptools.setup(name="AIFloodMaster",
                 version=Version,
                 description="贵仁-智能雨洪管理模型",
                 url="https://cloud.keepsoft.net/product",
                 include_package_data=True,
                 package_data={
                     "lstm_data": ["data/lstm-data/test-data/*.csv"],
                     "ddpg_data": [
                         "data/ddpg-swmm-data/obs_data_1month_all_controlled/*.inp",
                         "data/ddpg-swmm-data/obs_data_daily_fcsts/*.csv"
                     ]
                 },
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3.9"])
