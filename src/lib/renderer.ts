export const renderer = {
  heading(text: string, level: number): string {
    return `<h${level} class="heading">${text}</h${level}>`;
  },
  paragraph(text: string): string {
    return '<p class="content">' + text + '</p>\n';
  }
};
