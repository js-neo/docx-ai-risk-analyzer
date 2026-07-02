import type { Metadata } from "next";

import "./globals.css";

export const metadata: Metadata = {
  title: "DOCX AI Risk Analyzer",
  description:
    "Локальный анализ DOCX-документов по редакционным признакам AI-риска.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ru">
      <body>{children}</body>
    </html>
  );
}
