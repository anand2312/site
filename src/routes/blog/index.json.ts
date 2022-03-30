import fs from 'fs';
import path from 'path';
import grayMatter from 'gray-matter';

function getAllPosts() {
  try {
    return fs.readdirSync('static/posts/').map((fileName) => {
      const post = fs.readFileSync(path.resolve('static/posts', fileName), 'utf-8');
      return {
        slug: fileName.slice(0, -3),
        ...grayMatter(post).data
      };
    });
  } catch (e) {
    return [];
  }
}

export async function get() {
  return {
    status: 200,
    headers: {
      'Content-Type': 'application/json'
    },
    body: {
      posts: getAllPosts()
    }
  };
}
