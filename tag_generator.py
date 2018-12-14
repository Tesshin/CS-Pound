import glob
import os
import textwrap

post_directory = '_posts/'
tag_directory = 'tag/'

files = glob.glob(post_directory + '*.markdown')

all_tags = set()
for file in files:
    with open(file, 'r') as f:
        crawl = False
        for line in f:
            if crawl:
                current_tags = line.strip().split()
                if current_tags[0] == 'tags:':
                    all_tags.update(current_tags[1:])
                    crawl = False
                    break
            if line.strip() == '---':
                if not crawl:
                    crawl = True
                else:
                    crawl = False
                    break

old_tags = glob.glob(tag_directory + '*.markdown')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_directory):
    os.makedirs(tag_directory)

for tag in all_tags:
    tag_filename = tag_directory + tag.lower() + '.markdown'
    with open(tag_filename, 'a') as f:
        write_str = f'''\
        ---
        layout: tag
        title: 'Tag: {tag}'
        tag: {tag}
        robots: noindex
        ---\n'''
        write_str = textwrap.dedent(write_str)
        f.write(write_str)
        f.close()

print(f'{len(all_tags)} tags generated')
print(list(all_tags))
