import os
import requests
from tqdm import tqdm


class File:
	class Size:
		def find_file_size(self, path="C:\\", max_or_min="max"):
			size_path, size_list = self.__get_all_size(path)
			if max_or_min == "max":
				fsize = size_path[size_list.index(max(size_list))][0]
			elif max_or_min == "min":
				fsize = size_path[size_list.index(min(size_list))][0]
			else:
				raise ValueError("max_or_min参数只能填max或min")
			return self.__size_small(fsize, size_path, size_list)

		def __get_all_size(self, path):
			size_path = []
			for path, file_dir, files in os.walk(path):
				for file_name in files:
					size_path.append([os.path.getsize(os.path.join(path, file_name)), os.path.join(path, file_name)])
				for dir in file_dir:
					size_path.append([os.path.getsize(os.path.join(path, dir)), os.path.join(path, dir)])
			size_list = []
			for i in range(len(size_path)):
				size_list.append(size_path[i][0])
			return size_path, size_list

		def __size_small(self, fsize, size_path, size_list):
			if fsize < 1024:
				return [str(round(fsize, 2)) + 'B', size_path[size_list.index(max(size_list))][1]]
			else:
				KBX = fsize / 1024
				if KBX < 1024:
					return [str(round(KBX / 1024, 2)) + 'K', size_path[size_list.index(max(size_list))][1]]
				else:
					MBX = KBX / 1024
					if MBX < 1024:
						return [str(round(KBX / 1024, 2)) + 'M', size_path[size_list.index(max(size_list))][1]]
					else:
						GBX = MBX / 1024
						if GBX < 1024:
							return [str(round(MBX / 1024, 2)) + 'G', size_path[size_list.index(max(size_list))][1]]
						else:
							return [str(round(GBX / 1024, 2)) + 'T', size_path[size_list.index(max(size_list))][1]]

		def all_file_size(self, path="C:\\"):
			size_path, size_list = self.__get_all_size(path)
			for i in range(len(size_path)):
				size_path[i][0] = str(self.__size_small(int(size_path[i][0]), size_path, size_list)[0])
			return size_path

class Download:
	def Download_with_progress_bar(self,url,fname):
		resp = requests.get(url, stream=True)
		total = int(resp.headers.get('content-length', 0))
		with open(fname, 'wb') as file, tqdm(
				desc=fname,
				total=total,
				unit='iB',
				unit_scale=True,
				unit_divisor=1024,
		) as bar:
			for data in resp.iter_content(chunk_size=1024):
				size = file.write(data)
				bar.update(size)


file = File
size = file.Size()
download = Download()