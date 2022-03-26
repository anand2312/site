import fs from 'fs';
import path from 'path';
import grayMatter from 'gray-matter';
import { marked } from 'marked';

function getPost(filename: string): string {
  return fs.readFileSync(path.resolve('static/posts', `${filename}.md`), 'utf-8');
}

export async function get({ params }) {
  try {
    const post = getPost(params.slug);
    const renderer = new marked.Renderer();
    const { data, content } = grayMatter(post);
    const html = marked(content, { renderer });

    return {
      status: 200,
      headers: {
        'Content-Type': 'application/json'
      },
      body: {
        html: html,
        ...data
      }
    };
  } catch (e) {
    console.log(e);
    return {
      status: 404,
      body: {
        message: 'Not found'
      }
    };
  }
}
