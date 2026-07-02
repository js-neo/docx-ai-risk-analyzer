import { AnalyzerUploadForm } from "@/components/analyzer-upload-form";

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 px-6 py-10 text-slate-50">
      <div className="mx-auto flex max-w-6xl flex-col gap-8">
        <header className="max-w-3xl">
          <p className="text-sm font-medium uppercase tracking-[0.24em] text-cyan-300">
            DOCX AI Risk Analyzer
          </p>
          <h1 className="mt-4 text-4xl font-semibold tracking-tight text-white md:text-6xl">
            Анализ DOCX-документов по редакционным признакам AI-риска
          </h1>
          <p className="mt-5 text-lg leading-8 text-slate-300">
            Загрузите академический документ в формате DOCX. Сервис извлечёт
            текст, разделит его на блоки и покажет риск по клише, абстрактной
            лексике и структурной равномерности текста.
          </p>
        </header>

        <AnalyzerUploadForm />
      </div>
    </main>
  );
}
