import React from 'react';
import { LayoutDashboard, Database, TrendingUp } from 'lucide-react';
import { BarChart, Bar, XAxis, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Seg', total: 400 },
  { name: 'Ter', total: 300 },
  { name: 'Qua', total: 600 },
  { name: 'Qui', total: 800 },
  { name: 'Sex', total: 500 },
];

export default function App() {
  return (
    <div className="bg-darkBg min-h-screen text-white p-8">
      <header className="mb-10 flex justify-between items-center border-b border-white/10 pb-5">
        <h1 className="text-3xl font-black text-vibrant italic tracking-tighter">
          DATA PIPELINE ENGINE
        </h1>
        <div className="bg-cardBg px-4 py-1 rounded-full border border-vibrant/50 text-xs font-mono">
          STATUS: ONLINE
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        <Card title="Ingestão Total" value="1.240" icon={<Database size={20}/>} />
        <Card title="Última Carga" value="Hoje, 21:43" icon={<TrendingUp size={20}/>} />
        <Card title="Arquivos CSV" value="12" icon={<LayoutDashboard size={20}/>} />
      </div>

      <div className="bg-cardBg p-6 rounded-xl border border-white/5 h-80">
        <h2 className="text-vibrant font-bold mb-4 uppercase text-sm tracking-widest">Fluxo de Vendas (PostgreSQL)</h2>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <XAxis dataKey="name" stroke="#4b5563" fontSize={12} />
            <Tooltip contentStyle={{backgroundColor: '#0b0e14', border: '1px solid #00f2ff'}} />
            <Bar dataKey="total" fill="#00f2ff" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

function Card({ title, value, icon }) {
  return (
    <div className="bg-cardBg p-6 rounded-xl border border-white/5 hover:border-vibrant/20 transition-all">
      <div className="flex items-center gap-3 text-gray-400 mb-2 uppercase text-xs font-bold tracking-widest">
        {icon} {title}
      </div>
      <div className="text-3xl font-mono text-white">{value}</div>
    </div>
  );
}