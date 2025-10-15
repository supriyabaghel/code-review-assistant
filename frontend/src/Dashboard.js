import React, { useRef, useState } from "react";
import { UploadIcon } from "./icons";

console.log("✅ Dashboard.js loaded");

function Dashboard() {
  const fileInputRef = useRef(null);
  const [file, setFile] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState(null);

  const acceptedTypes = [
    "py", "js", "ts", "java", "cpp", "cs", "go", "rs", "kt", "zip", "tar.gz",
  ];

  const handleFileChange = (e) => {
    const chosenFile = e.target.files?.[0];
    if (!chosenFile) return;

    const ext = chosenFile.name.split(".").pop()?.toLowerCase() || "";
    if (!acceptedTypes.includes(ext)) {
      setError("Unsupported file type");
      setFile(null);
      e.target.value = "";
      return;
    }

    setError("");
    setFile(chosenFile);
  };

  const handleUploadClick = () => {
    fileInputRef.current?.click();
  };

  const handleSubmit = async () => {
    if (!file) return;
    console.log("📤 Uploading file to backend…");
    setLoading(true);
    setError("");
    setReport(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/review", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error(`Server returned ${response.status}`);

      const data = await response.json();
      console.log("✅ Full backend response:", data);
      setReport(data);
    } catch (err) {
      console.error(err);
      setError("Failed to generate report. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-gradient-to-br from-[#CBE5FF] to-[#0A64D1] p-10">
      <div className="bg-white/95 rounded-3xl shadow-2xl w-full max-w-7xl p-16 flex flex-col items-center text-center space-y-10 overflow-y-auto max-h-[95vh] border border-gray-200">
        {/* Title */}
        <h1 className="text-6xl font-extrabold text-gray-900 drop-shadow-lg">
          Code Review Assistant
        </h1>

        {/* Upload bar */}
        <div
          onClick={handleUploadClick}
          className="flex items-center w-full max-w-4xl bg-gray-50 shadow-inner rounded-3xl px-8 py-6 cursor-pointer border border-gray-300 hover:border-blue-500 focus-within:ring-4 focus-within:ring-blue-300 transition duration-200"
          role="button"
          aria-label="Upload your code file"
        >
          <div className="flex items-center justify-center bg-blue-100 text-blue-600 rounded-2xl w-16 h-16 mr-6">
            <UploadIcon className="w-10 h-10" />
          </div>
          <div className="flex-1 text-left text-gray-600 text-2xl truncate">
            {file ? file.name : "Upload your code file"}
          </div>
          <input
            type="file"
            accept=".py,.js,.ts,.java,.cpp,.cs,.go,.rs,.kt,.zip,.tar.gz"
            ref={fileInputRef}
            onChange={handleFileChange}
            className="hidden"
          />
        </div>

        {error && <p className="text-red-600 text-2xl">{error}</p>}

        {/* Button */}
        <button
          onClick={handleSubmit}
          disabled={!file || loading}
          className={`w-96 h-20 text-2xl font-bold text-white rounded-full transition-all duration-300 focus:ring-4 focus:ring-offset-2 focus:ring-blue-400
            ${
              file && !loading
                ? "bg-gradient-to-r from-[#4EA7FF] to-[#0A4FBF] hover:brightness-110"
                : "bg-gray-400 cursor-not-allowed"
            }`}
        >
          {loading ? (
            <span className="flex items-center justify-center gap-4">
              <svg
                className="animate-spin h-8 w-8 text-white"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                ></circle>
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
                ></path>
              </svg>
              Generating…
            </span>
          ) : (
            "View Report"
          )}
        </button>

        {/* Report */}
        {report && (
          <div className="mt-6 w-full bg-gray-50 rounded-3xl p-10 shadow-inner border border-gray-200 text-left animate-fadeIn text-xl leading-relaxed">
            {/* Summary */}
            {report.report?.analysis?.summary && (
              <section className="mb-8">
                <h2 className="text-4xl font-bold text-blue-700 mb-4">
                  🧾 Summary
                </h2>
                <p className="text-gray-800 text-2xl">
                  {report.report.analysis.summary}
                </p>
              </section>
            )}

            {/* Issues */}
            {report.report?.analysis?.issues?.length > 0 && (
              <section className="mb-8">
                <h2 className="text-4xl font-bold text-red-700 mb-4">
                  ⚠️ Issues
                </h2>
                <ul className="space-y-4 text-2xl text-gray-900">
                  {report.report.analysis.issues.map((issue, i) => (
                    <li
                      key={i}
                      className="p-6 bg-white rounded-2xl border border-gray-200 shadow-md"
                    >
                      <p>
                        <strong>Line {issue.line}</strong> —{" "}
                        <span className="font-semibold">{issue.message}</span>
                      </p>
                      <p className="text-gray-700 mt-2">
                        💡 {issue.suggested_fix}
                      </p>
                      <p className="text-lg text-gray-500 mt-2">
                        Severity:{" "}
                        <span
                          className={
                            issue.severity === "high"
                              ? "text-red-600 font-bold"
                              : "text-yellow-600 font-semibold"
                          }
                        >
                          {issue.severity}
                        </span>{" "}
                        | Confidence: {Math.round(issue.confidence * 100)}%
                      </p>
                    </li>
                  ))}
                </ul>
              </section>
            )}

            {/* Suggestions */}
            {report.report?.analysis?.suggestions?.length > 0 && (
              <section className="mb-8">
                <h2 className="text-4xl font-bold text-green-700 mb-4">
                  💡 Suggestions
                </h2>
                <ul className="space-y-3 text-2xl text-gray-900">
                  {report.report.analysis.suggestions.map((s, i) => (
                    <li
                      key={i}
                      className="p-5 bg-white rounded-2xl border border-gray-200 shadow-md"
                    >
                      <strong>{s.category}:</strong> {s.message}
                    </li>
                  ))}
                </ul>
              </section>
            )}

            {/* Metrics */}
            {report.report?.analysis?.metrics && (
              <section className="mb-8">
                <h2 className="text-4xl font-bold text-purple-700 mb-4">
                  📊 Metrics
                </h2>
                <pre className="bg-white p-6 rounded-2xl border border-gray-200 text-2xl text-gray-900 overflow-x-auto whitespace-pre-wrap">
                  {JSON.stringify(report.report.analysis.metrics, null, 2)}
                </pre>
              </section>
            )}

            {/* Model Info */}
            {report.report?.analysis?.llm_metadata && (
              <p className="text-gray-500 text-xl mt-8">
                🤖 Generated by {report.report.analysis.llm_metadata.model}
              </p>
            )}
          </div>
        )}

        {/* Footer */}
        <footer className="text-2xl text-gray-600 mt-10 font-semibold">
          © Created by <span className="font-bold text-blue-700">Supriya</span>
        </footer>
      </div>
    </div>
  );
}

export default Dashboard;
