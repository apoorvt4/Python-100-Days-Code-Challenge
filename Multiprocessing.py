import multiprocessing
import multiprocessing.process
import requests

def downloadeFile(url, name):
     print(f"Started Dowloading{name}")
     r = requests.get(url)
     open(f'files2/file{name}.jpg', 'wb').write(r.content)
     print(f"Finished Dowloading{name}")
    

url = "https://images.unsplash.com/photo-1721332150382-d4114ee27eff?q=80&w=435&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

pros = []
for i in range(1):
     p = multiprocessing.process(target=downloadeFile, args=[url, i])
     p.start()
     pros.append(p)

for p in pros:
     p.join()